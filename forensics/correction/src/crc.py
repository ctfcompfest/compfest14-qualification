import os
import binascii
import struct

misc = open("m00n.png","rb").read()

for i in range(1921):
    data = misc[12:16] + struct.pack('>i',i) + struct.pack('>i',(i//9) * 16) + misc[24:29]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == 0xCE13B260:
        print(i)