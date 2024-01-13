
with open("bin.txt", "r") as src:
    res = ""
    for i in src.readlines():
        cln_wrd = i.strip();
        for j in range(0, len(cln_wrd), 8):
            one_bit = chr(int(cln_wrd[j:j+8],2))
            if 0 <= ord(one_bit) <= 127:
                res += one_bit
                
    print(res)            