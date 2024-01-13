flag=b"COMPFEST14{0k_n0_m04r_d3bu6_m0d3_n3xT_ti3m__mayB_ba3e31290d}"

rt1=b"I really like pineapples on pizza.... Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed suscipit libero ac felis commodo vulputate. Suspendisse risus sapien, accumsan quis dictum sed, hendrerit quis sem."
rt2=b"Vanilla tastes better than chocolate. Praesent sit amet blandit sapien. Duis hendrerit blandit magna sit amet blandit. Curabitur vulputate, quam a posuere euismod, leo erat malesuada nunc, at euismod massa neque nec sem."

out = b''

for i, j in enumerate(flag):
	out += chr(j^rt1[i]^rt2[i]).encode()

for i in out:
	print(i, end=', ')