# Writeup Lisandro martineZ

Deskripsi soal mengindikasikan bahwa *files* yang diberikan telah melalui sebuah skema kompresi. Namun, skema kompresi apa yang digunakan? Sebelum menganalisis *files* yang diberikan, kita dapat memanfaatkan *hints* yang diberikan pada judul dan deskripsi soal (~~yak sedikit dukun, tapi kalau sekali google juga yang muncul paling atas ini kok hehe~~). Pertama, pada judul soal, huruf L dan Z ditulis dalam kapital. Kedua, deskripsi soal menggambarkan seseorang yang selalu menang. ~~Dengan bantuan dukun~~, dapat disimpulkan bahwa skema kompresi yang digunakan adalah salah satu yang cukup terkenal, yaitu **L**empel-**Z**iv _**loseless**_ *data compression*. Satu-satunya huruf yang ditulis dalam kapital pada deskripsi soal, yaitu 'W', sebenarnya juga merupakan *hint* yang mengindikasikan LZW sebagai varian Lempel-Ziv yang digunakan. Namun, tanpa menyadari *hint* tersebut, kita juga dapat melakukan analsis melalui salah satu *file* yang diberikan, yaitu lorem. 

![img](https://cdn.discordapp.com/attachments/902951430153981993/1002566925534105750/unknown.png)

Terlihat bahwa beberapa *bytes* awal dari *file* adalah kata "Lorem" yang setiap karakternya diawali *null byte*. Menulusuri *byte-byte* selanjutnya, dapat diasumsikan bahwa *file* ini berisi teks *lorem ipsum* yang umum diawali dengan kalimat "Lorem ipsum dolor sit amet". Namun, ada beberapa *string* yang hilang, seperti "m " pada "ipsum " dan "or" pada "dolor". Karena *file* telah melalui sebuah skema kompresi, maka bisa diasumsikan hal tersebut terjadi karena *string* tersebut sudah muncul sebelumnya, yaitu "m " pada "Lorem " dan "or" pada "Lorem". Akan tetapi, mengapa *string* dengan panjang satu kembali muncul walaupun sudah muncul sebelumnya? Dari sini, kita bisa langsung menyimpulkan kalau skema kompresi yang digunakan adalah LZW. Pada LZW, sebuah *dictionary* yang berisi semua kemungkinan karakter akan diinisialisasi terlebih dahulu. Secara umum, *dictionary* tersebut akan berisi 256 karater 8-bit, dimulai dari yang memiliki kode *unicode* 0 s/d 255. Selanjutnya proses kompresi akan dimulai dengan menginisialisasi *string* `S` sebagai *byte* pertama. Bila `S` ada pada *dictionary*, maka konkatenasi `S` dengan satu *byte* selanjutnya, kita anggap sebagai `c`, yang menghasilkan `S|c`. Bila `S|c` juga ditemukan pada *dictionary*, maka `S = S|c` dan ulangi proses sebelumnya. Hingga ketika `S|c` tidak ditemukan pada *dictionary*, nilai `S` pada dictionary akan menjadi *output*, tambahkan `S|c` ke *dictionary*, serta `S = c`. Pada LZW, ukuran *output* akan menyesuaikan dengan ukuran *dictionary*. Pada kasus ini, dengan adanya karakter yang diawali *null byte*, bisa diasumsikan bahwa setiap *output* memiliki ukuran 16 bit. Kira-kira, begini proses kompresi yang terjadi pada kalimat "Lorem ipsum dolor ".

| S     | In dict? | Add to dict | Output 
|:-----:|:--------:|:-----------:|:------:
| `L`   | ✓  |             |   
| `Lo`  | ✗  | `256-Lo`    | 76 (`L`) 
| `o`   | ✓  |             |
| `or`  | ✗  | `257-or`    | 111 (`o`)
| ...   | ... | ...         | ...
| `m`   | ✓  |             |
| `m `  | ✗  | `260-m `    | 109 (`m`)
| ...   | ...      | ...         | ...
| `m`   | ✓  |             |
| `m `  | ✓  |             |
| `m d` | ✗  | `266-m d`   | 260 (`m `)
| `o`   | ✓  |             |
| `or`  | ✓  |             |
| `or ` | ✗  | `270-or `   | 257 (`or`)

Dengan demikian, kita bisa melakukan dekompresi pada file dengan me-*reverse* algoritma kompresi yang sudah diketahui (atau ya di gugel juga banyak).
```python
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
```

Setelah dekompresi selesai dilakukan, sudah terlihat bahwa *chall* merupakan sebuah bytecode python. Dengan membaca referensi mengenai instruksi pada bytecode python, salah satunya [ini][1], kurang lebih seperti [ini][2] hasilnya dalam python. Fungsi `encrypt` dapat di-*reverse* karena merupakan *affine cipher*, `werivy(inp)` dapat diselesaikan menggunakan `z3`, `key(n)` merupakan bilangan fibonacci ke-n, dan sisanya hanya operasi `xor` biasa.

[1]: https://docs.python.org/3/library/dis.html
[2]: ../src/chall.py