from Crypto.Util.number import long_to_bytes

out = b''

with open("out.txt", "r") as f:
	cont = f.read().split()
	for i, j in enumerate(cont):
		if(i % 9 == 0 ): continue
		curr = int(j, 8)
		out = out + long_to_bytes(curr)[::-1]

print(out)
