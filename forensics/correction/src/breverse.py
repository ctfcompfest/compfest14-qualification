
print("this is a byte reverser for non-plaintext data.\nplease input the valid data!")

file_name = input("insert src file >> ")
out_name = input("insert out file >> ")


src = open(file_name, "rb").read();
rev_arr = [];

for i in src:
    rev_arr.insert(0,i);

target = open(out_name, "wb")  
target.write(bytearray(rev_arr));


