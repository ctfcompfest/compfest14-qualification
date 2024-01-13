from lzw import compress
import py_compile, dis

py_compile.compile("chall.py", "chall_c.pyc")

import chall_c
with open("chall_b", 'w') as f:
    dis.dis(chall_c, file=f)

compress("chall_b", "chall")