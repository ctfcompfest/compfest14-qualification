from des_lib import *
from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l

def S(bits, i):
    return '{0:04b}'.format(S_BOXES[i][int(bits[0] + bits[-1], 2)][int(bits[1:-1], 2)])

def xor(a, b):
    return ''.join([str(int(i) ^ int(j)) for i, j in zip(a, b)])

def F(bits, key):
    e = ''.join([bits[i] for i in EXPANSION_FUNCTION])
    key_bits = bin(b2l(key))[2:].zfill(48)

    xored = xor(key_bits, e)
    s = ''.join([S(xored[i:i+6], i//6) for i in range(0, len(xored), 6)])

    return ''.join([s[i] for i in P])

def decrypt(ctxt, key):
    permuted_final = bin(int(ctxt, 16))[2:].zfill(64)
    r_l = ''.join([i[1] for i in sorted(list(zip(FINAL_PERMUTATION, permuted_final)))])
    right = r_l[32:]
    left = xor(r_l[:32], F(right, key))
    permuted = left + right
    message_bits = ''.join([i[1] for i in sorted(list(zip(INITIAL_PERMUTATION, permuted)))])
    return int(message_bits, 2).to_bytes(8, 'big')

def default_format(s):
    format = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz-0123456789{}"
    for i in s:
        if i not in format:
            return False
    return True

with open('flag.enc', 'r') as file:
    hex_cipher = file.read().split()[-1]

# Reverse some of the required parameters from known parts of the flag and the encrypted flag
known_plain = b"COMPFEST"
hex_known = hex_cipher[:16]

known_bits = bin(int(hex_known, 16))[2:].zfill(64)
rl = ''.join([i[1] for i in sorted(list(zip(FINAL_PERMUTATION, known_bits)))])

xored_l = rl[:32]
right = rl[32:]

message_bits = bin(b2l(known_plain))[2:].zfill(64)
left = ''.join([message_bits[i] for i in INITIAL_PERMUTATION])[:32]

eff = xor(xored_l, left)
s = ''.join([i[1] for i in sorted(list(zip(P, eff)))])
s = [int(s[i:i+4], 2) for i in range(0, len(s), 4)]

exp = ''.join([right[i] for i in EXPANSION_FUNCTION])

cipher_parts = hex_cipher[16:32]

# Bruteforce all of the possible key 
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    for f in range(4):
                        for g in range(4):
                            for h in range(4):
                                row = [bin(i)[2:].zfill(2) for i in [a, b, c, d, e, f, g, h]]
                                col = [bin(S_BOXES[i][int(j,2)].index(s[i]))[2:].zfill(4) for i, j in zip(range(8), row)]
                                temp = ''.join([r[0] + c + r[1] for r, c in zip(row, col)])
                                key = l2b(int(xor(temp, exp), 2))
                                try:
                                    test = decrypt(cipher_parts, key).decode()
                                    if '14{' in test[:3]:
                                        flag = ''                                    
                                        for i in range(16, len(hex_cipher), 16):
                                            partial = decrypt(hex_cipher[i:i+16], key).decode()
                                            valid = default_format(partial)
                                            if valid:
                                                flag += partial
                                            else:
                                                break
                                            
                                        if valid:
                                            print("COMPFEST" + flag)                                        
                                except:
                                    continue

