# Writeup 3(3DES)

Perhatikan bahwa pada fungsi `encrypt(plain, n)` terdapat parameter `n` yang berpengaruh terhadap banyaknya ronde dalam sebuah enkripsi. 
```python
def encrypt(plain, n):
    ...
    for i in range(n):
        l.append(r[i])
        r.append(xor(l[i], F(r[i], KEY[i+1])))
    ...
```
Selanjutnya, perhatikan juga bahwa terdapat sembilan hasil enkripsi `FLAG` yang didapatkan dari fungsi `encrypt(plain, n)` dimana nilai `n` adalah `sumn(a), a = 1, 2, 3, ..., 9`. 
```python
def sumn(a):
    return int((1 << 4) - 0xf / 8 * (a - 1))
```
`sumn(9)` akan mengembalikan nilai `1`, yang berarti hasil enkripsi `FLAG` terakhir hanya melewati satu ronde saja. Selain itu, karena tidak ada informasi tambahan mengenai format flag, maka setidaknya telah diketahui 11 karakter pertamanya, yaitu `COMPFEST14{`. Kemudian, perhatikan juga bahwa enkripsi `FLAG` dilakukan per delapan karakter.
```python
with open('flag.enc', 'w') as fout:
    for i in range(1,10):
        cipher = b''.join([encrypt(FLAG[j:j+8], sumn(i)) for j in range(0, len(FLAG), 8)])
        print(cipher.hex(), file=fout)
```
Dari sini bruteforce dan sedikit reversing dapat dilakukan untuk menemukan key yang sesuai dan kemudian melakukan dekripsi pada `FLAG`.