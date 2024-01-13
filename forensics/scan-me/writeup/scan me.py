from pyzbar.pyzbar import decode
from PIL import Image

def decode_qr (folder_dir,n,list_of_text):
   for file_name in range(1,n):
    decocdeQR = decode(Image.open(folder_dir + str(file_name) +'.png'))
    list_of_text.append(decocdeQR[0].data.decode('ascii'))


# List penampung hasil decode qr code
sanitized = []

# folder directory qr code
folder = r'C:\Users\ASUS\Desktop\New folder\Solusi\scan-me\qr\\'

decode_qr(folder,829,sanitized)

qr_data = ""

# for loop untuk meng-ekstrak nilai 2 bit dari semua qr code
for i in sanitized:
    qr_data+= i[2:]
print(qr_data)


