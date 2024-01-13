from itertools import combinations
from Crypto.Util import Padding, number
from Crypto.Cipher import AES
from z3 import *
import hashlib, time

class LFSR:
    def __init__(self, state, taps):
        self.state = state
        self.taps = [len(state) - t for t in taps]

    def clock(self):
        out = self.state[0]
        self.state = self.state[1:] + [sum(self.state[t] for t in self.taps)%2]
        return out

class Generator:
    def __init__(self, seed):
        self.seed = seed
        assert len(self.seed) == 99
        self.lfsr = [LFSR(self.seed[:37], [37, 5, 4, 3, 2, 1]), 
                     LFSR(self.seed[37:56], [19, 6, 2, 1]), 
                     LFSR(self.seed[56:80], [24, 23, 22, 17]), 
                     LFSR(self.seed[80:], [19, 6, 2, 1])]
    
    def combined_clock(self):
        bits = [l.clock() for l in self.lfsr]
        return If(bits[1]==1, bits[0], If(bits[3]==1, bits[2], bits[0]))

with open('out.txt', 'r') as f:
    out = f.readlines()
    stream = eval(out[0])
    ctxt = out[1]

start = time.time()

print("[*] Finding initial state of LFSR_0")
# a == out -> 87.5%
found = False; i = 0
while not found and i < 37:
    for diff in combinations(range(37), i):
        seed_temp = [1^stream[i] if i in diff else stream[i] for i in range(37)]
        lfsr = LFSR(seed_temp, [37, 5, 4, 3, 2, 1])
        same = sum(s == lfsr.clock() for s in stream)
        if same >= 224:
            seed_part1 = seed_temp
            found = True
            break
    i += 1

# a != out -> c == out
seed_part3 = [None] * 24
for i in range(24):
    if seed_part1[i] != stream[i]:
        seed_part3[i] = stream[i]

seed_part1 = [BitVec(i, 1) for i in seed_part1]

print("[*] Finding flag")
# c == out -> 62.5%
not_found = [i for i in range(24) if seed_part3[i] == None]
found = False; j = 0
while not found and j < len(not_found):
    for diff in combinations(not_found, j):
        seed_temp = seed_part3[:]
        for i in not_found:
            if i in diff:
                seed_temp[i] = 1^stream[i]
            else:
                seed_temp[i] = stream[i]

        lfsr = LFSR(seed_temp, [24, 23, 22, 17])
        same = sum(s == lfsr.clock() for s in stream)
        if same >= 160:
            seed = seed_part1 + [BitVec(f's_{i}', 1) for i in range(19)] \
                  + [BitVec(i, 1) for i in seed_temp] + [BitVec(f's_{i}', 1) for i in range(19, 19+19)]
            G = Generator(seed)
            solver = Solver()
            for s in stream:
                solver.add(s == G.combined_clock())
            try:
                assert solver.check() == sat
                key = int(''.join(str(solver.model()[s]) for s in seed), 2)
                key = hashlib.sha256(number.long_to_bytes(key)).digest()[:16]
                iv = bytes.fromhex(ctxt[:32])
                ctxt = bytes.fromhex(ctxt[32:])
                cipher = AES.new(key, 2, iv)
                ctxt = Padding.unpad(cipher.decrypt(ctxt), 16)
                print('[+] FLAG: ' + ctxt.decode())
                end = time.time()
		# It takes around 10 minutes on average to run the script on author's machine
                print(f'[*] Solved in {(end-start)//60} minute(s) {round((end-start)%60)} second(s)')
                found = True
                break
            except:
                continue
    j += 1
