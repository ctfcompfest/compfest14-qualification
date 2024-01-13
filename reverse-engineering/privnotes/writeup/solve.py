patt = [92, 14, 81, 92, 75, 69, 94, 13, 101, 57, 97, 47, 107, 12, 62, 59, 84, 124, 37, 33, 112, 19, 117, 40, 35, 116, 120, 28, 117, 54, 125, 38, 82, 33, 105, 51, 84, 95, 104, 116, 32, 109, 65, 26, 106, 101, 42, 68, 91, 54, 37, 61, 100, 57, 55, 50, 40, 53, 113, 51, 59, 75, 125, 63, 20, 36, 71, 84, 59, 24, 28, 82, 31, 49, 109, 74, 16, 46, 88, 114, 119, 110, 51, 65, 113, 49, 67, 48, 124, 120, 80, 119, 30, 94, 17, 116, 124, 44, 101, 30, 113, 83, 70, 79, 122, 55, 101, 120, 103, 64, 86, 73, 70, 53, 48, 107, 46, 49, 99, 29, 117, 43, 58, 105, 54, 119, 25, 14, 68, 107, 14, 121, 62, 86, 17, 18, 33, 12, 56, 62, 50, 36, 32, 69, 110, 18, 29, 12, 34, 72, 61, 23, 24, 43, 101, 94, 52, 51, 107, 60, 106, 77, 49, 15, 78, 97, 39, 59, 96, 72, 24, 82, 69]
rt1=b"I really like pineapples on pizza.... Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed suscipit libero ac felis commodo vulputate. Suspendisse risus sapien, accumsan quis dictum sed, hendrerit quis sem."
rt2=b"Vanilla tastes better than chocolate. Praesent sit amet blandit sapien. Duis hendrerit blandit magna sit amet blandit. Curabitur vulputate, quam a posuere euismod, leo erat malesuada nunc, at euismod massa neque nec sem."
out = ""
for i, j in enumerate(patt):
    for k in range(128):
        if(k^rt1[i]^rt2[i] == j):
            out += chr(k)
    if(out[-1] == "}"): break
print(out)