from z3 import *
import os, re, string

with open('chall', 'rb') as fin:
    compressed = fin.read()

    # Membaca karakter per dua byte karena output kompresi sebesar 16 bit.
    compressed = [int.from_bytes(compressed[i:i+2], 'big') for i in range(0, len(compressed), 2)]

# Inisialisasi dictionary dengan pointer:string
d = {i:bytes([i]) for i in range(256)}

dict_index = 256
buffer, decompressed = b"", b""
for i in compressed:
    # Antisipasi buffer dengan karakter berulang
    if i not in d:
        d[i] = buffer + bytes([buffer[0]])

    # Konkatenasi buffer dengan satu byte setelahnya, kemudian tambahkan ke dict
    if buffer != b"":
        d[dict_index] = buffer + bytes([d[i][0]])
        dict_index += 1

    decompressed += d[i]
    buffer = d[i]

with open('chall_b', 'wb') as f:
    f.write(bytes(decompressed))

# Improved fibonacci
d = {0:1, 1:1}
def key(n):
    if n in d:
        return d[n]
    a = key(n-2) + key(n-1)
    d[n] = a
    return a

def decrypt(x):
    return (x - 22) * 103 % 256

# Get werivy bytecode
with open('chall_b', 'r') as f:
    tes = f.read(4530)
    werivy = f.read(53698).split('\n\n')
    
s = Solver()
inp = [Int(f'enc[{i}]') for i in range(40)]
for i in inp:
    s.add(i >= 0)
    s.add(i <= 256)

# Solve werivy
for i in range(len(werivy)):
    ops = []
    add_i = werivy[i].find("ADD")
    sub_i = werivy[i].find("SUBTRACT")
    while add_i + sub_i != -2:
        if add_i != -1:
            ops.append((add_i, '+'))
            add_i = werivy[i].find("ADD", add_i+1)
        if sub_i != -1:
            ops.append((sub_i, '-'))
            sub_i = werivy[i].find("SUBTRACT", sub_i+1)
        
    ops.sort()
    nums = re.findall('\(\-*\d+\)', werivy[i])

    eq = "".join(f'({nums[i*2][1:-1]} * inp[{nums[i*2+1][1:-1]}]) {ops[i][1]} ' for i in range(4))
    eq += f"({nums[-3][1:-1]} * inp[{nums[-2][1:-1]}]) == {nums[-1][1:-1]}"
    exec(f's.add({eq})')

s.check()
enc = [0]*40
for i in str(s.model()).split('\n'):
    exec(i.strip(' '+string.punctuation))

assert enc == [132, 219, 160, 6, 139, 7, 77, 126, 223, 42, 144, 20, 7, 130, 196, 207, 188, 62, 31, 113, 46, 219, 100, 161, 43, 99, 183, 194, 249, 23, 201, 111, 121, 46, 234, 198, 120, 197, 128, 192]

flag = [decrypt(enc[0]) ^ key(0)]
for i in range(1, 40):
    flag += [decrypt(enc[i] ^ flag[-1]) ^ (key(i) & 0xff)]
print(bytes(flag))



