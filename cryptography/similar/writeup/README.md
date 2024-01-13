# Writeup similar
Tujuan utama dari *challenge* ini adalah me-*recover* `seed` yang digunakan sebagai `key` dalam proses enkripsi `flag`. `Seed` akan digunakan sebagai *initial state* dari empat buah LFSR. Pada `out.txt` diberikan 256-bit *stream* yang dihasilkan `combined_clock()`. 
```python
def combined_clock(self):
    bits = [l.clock() for l in self.lfsr]
    return bits[0] if bits[1] else bits[2] if bits[3] else bits[0] 
```
*Output* dari `combined_clock()` merupakan kombinasi *output* empat LFSR yang di-*clock* secara bersamaan. Selanjutnya, perhatikan tabel yang menunjukkan kombinasi *output* dari empat LFSR dengan `combined_clock()` di bawah ini.

| `bits[0]` | `bits[1]` | `bits[2]` | `bits[3]` | Output 
|:---------:|:---------:|:---------:|:---------:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

Terlihat bahwa 14 dari 16 kombinasi yang ada, `bits[0]` memiliki nilai yang sama dengan *output*. Dari sini dapat diketahui kalau $`LFSR_0`$ memiliki kemungkinan sekitar 87.5% untuk menghasilkan *output stream* yang sama dengan `combined_clock()`. Hal ini juga berarti 37 bit *stream* pertama yang dihasilkan `combined_clock()` tidak akan jauh berbeda dengan *initial state* $`LFSR_0`$. Maka, *bruteforce* dapat dilakukan dimulai dengan menentukan *initial state* yang memiliki perbedaan 0 bit, 1 bit, 2 bit, dan seterusnya dengan *output stream* (1). Kemudian, bentuk LFSR (2) dan cek apakah *output stream* yang dihasilkan memiliki kesamaan sekitar 87.5% (3).
```python
found = False; i = 0
while not found and i < 37:
    for diff in combinations(range(37), i):
        seed_temp = [1^stream[i] if i in diff else stream[i] for i in range(37)] # 1
        lfsr = LFSR(seed_temp, [37, 5, 4, 3, 2, 1]) # 2
        same = sum(s == lfsr.clock() for s in stream) # 3
        if same >= 224:
            seed_part1 = seed_temp
            found = True
            break
    i += 1
```
Setelah ditemukan, perhatikan juga fakta bahwa *output* dari `combined_clock()` hanya ada dua kemungkinan, yaitu `bits[0]` atau `bits[2]`. Artinya, kalau ada *output* tidak sesuai dengan yang dihasilkan $`LFSR_0`$, sudah pasti *output* tersebut dihasilkan $`LFSR_2`$.
```python
seed_part3 = [None] * 24
for i in range(24):
    if seed_part1[i] != stream[i]:
        seed_part3[i] = stream[i]
```
Selanjutnya, *initial state* $`LFSR_2`$ dapat ditentukan menggunakan cara yang sama ketika menentukan *initial state* $`LFSR_0`$. Namun, karena tingkat kesesuaiannya hanya 62.5%, perbedaan antara *seed* yang mungkin tidak terlalu berpengaruh. Jadi, perlu dicoba semua kemungkinan *seed* yang memenuhi. Hal ini masih memungkinkan karena ukuran *seed* dari $`LFSR_2`$ hanya 24 bit, lebih tepatnya 21 karena sudah ada 3 bit yang ditemukan pada langkah sebelumnya. Terakhir, untuk *initial state* dari $`LFSR_1`$ dan $`LFSR_3`$ dapat diserahkan kepada `z3`.