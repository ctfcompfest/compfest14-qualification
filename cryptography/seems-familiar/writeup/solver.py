
import string
from time import sleep
from pwn import remote

countt = 0

def send(msg):
    print("sending " + msg)
    io.recvuntil(b"> ")
    io.sendline(b"2")
    io.recvuntil(b"= ")
    io.sendline(bytes(msg, encoding="utf-8"))
    response = io.recvline().decode(encoding="utf-8")
    assert response.find(": ") != -1, response
    return response[response.find(":") + 2:-1]

ip = "localhost"
port = 12688

plaintext = ''
characters = string.printable
io = remote(ip, port)
while True:
    tmp = ""
    for i in range(15, -1, -1):
        suppose = bytes('a'*i, encoding='utf-8').hex()
        countt += 1
        response = send(suppose)
        for j in characters:
            hexx = hex(ord(j))[2:].zfill(2)
            payload = suppose  + plaintext + tmp + hexx
            countt += 1
            response_check = send(payload)

            block_check = response_check[len(plaintext):len(plaintext) + 32]
            block_suppose = response[len(plaintext):len(plaintext) + 32] 
            if (block_check == block_suppose):
                tmp += hexx
                break
    plaintext += tmp
    if tmp == "":
        print(bytes.fromhex(plaintext).decode('utf-8'))
        print(countt)
        break