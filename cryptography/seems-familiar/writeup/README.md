# Writeup Seems Familiar

## tl;dr
* ECB Oracle attack (atau known plaintext attack)

Penjelasan detail:<br>

Dari keempat menu, hanya menu `Encrypt a message` dan menu `Exit`. `Exit` cukup straightforward sesuai namanya sehingga kita hanya perlu menganalisa menu `Encrypt`.<br>

## Alur Analisis 

1. Berdasarkan deskripsi, sistem ini menggunakan enkripsi berdasarkan **AES** sehingga **setiap block enkripsi teridiri dari 16 bytes** (16 karakter)
2.  Langkah selanjutnya adalah kita perlu mode operasi AES apa yang digunakan dalam sistem ini. Akan tetapi, dari sekian banyak mode enkripsi AES, kita hanya bisa menyirikan mode ECB dari fungsi enkripsinya saja. Berikut penjelasannya.
3. Berikut ini diagram enkripsi AES ECB,
   ![Diagram Enkripsi ECB (dari wikipedia)](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/ECB_encryption.svg/601px-ECB_encryption.svg.png "Diagram Enkripsi ECB (dari wikipedia)")<br>
   Berbeda dengan mode operasi lainnya, AES ECB tidak bersifat propagating, artinya, enkripsi setiap blok tidak dipengaruhi oleh blok lainnya. Posisi blok plaintext yang dienkripsi akan selalu menghasilkan ciphertext yang sama, di manapun posisi blok plaintext itu berada. Kemudian kita cek apakah ciri tersebut ada pada sistem ini.<br>
   ![Contoh Enkripsi ECB](/writeup/img/contoh_ecb.png "Contoh Enkripsi ECB")
   > Dapat dilihat bahwa ketika blok A dan blok B ditukar posisi, cipher A dan cipher B bertukar posisi juga dengan cipher yang sama sehingga **sistem ini menggunakan enkripsi ECB.**

1.  Perhatikan gambar berikut.<br>
   ![Cipher tambahan](/writeup/img/cipher_tambahan.png "Cipher tambahan")
   Menu `Encrypt` hanya menerima input hex. Akan tetapi, jika kita beri empty input, kita tetap mendapatkan suatu cipher. Panjang ciphertext memiliki panjang yang jauh lebih panjang dibandingkan dengan panjang plaintext yang dimasukkan. Hal itu sangat mencurigakan karena **panjang plaintext (dengan padding blok) akan selalu sama dengan panjang ciphertext**. Cipher tambahan yang kita berikan dalam input kosong dan 16 byte juga sama. Oleh karena itu, dapat kita asumsikan bahwa sistem menambahkan cipher setelah cipher input yang kita berikan. 

5. Karena kita tidak memiliki informasi lain, mari kita pecahkan apa cipher yang ditambahkan dengan metode Known-Plaintext Attack agar kita mendapatkan informasi dari cipher tersebut.

## Alur Known-Plaintext Attack dalam AES ECB

> Sumber penjelasan ada [di sini](https://crypto.stackexchange.com/questions/42891/chosen-plaintext-attack-on-aes-in-ecb-mode)
1. Kita sudah tahu bahwa ciphertext asing akan selalu ditambahkan setelah ciphertext dari input. Block ciphertext yang kita input juga dapat kita kontrol sepenuhnya dan expect hasilnya. Hal ini dinamakan dengan `Encryption Oracle`
2. Pertama kita harus kirim karakter apapun sebanyak 15 karakter, sehingga kita tahu bahwa hasil dekripsi akan menghasilkan pesan di bawah ini (dengan karakter 'a').
   ```
    plain = 'a'*15
    
    Block 1          Block 2  Block 3
    |aaaaaaaaaaaaaaa?|?......?|?......?|
    |----known-----||--m1---|

    cipher (misal) --> 892oaksm3ud2lk4n 
   ```
3. Setelah itu, kita harus mengenkripsi 15 karakter barusan, dan 1 karakter tambahan yang kita bruteforce berulang kali **hingga cipher yang dihasilkan sama dengan cipher enkripsi 15 karakter pada nomor `2`.**
      ```
    # loop 1
    plain = 'a'*15 + a
    
    Block 1          Block 2  Block 3
    |aaaaaaaaaaaaaaaa|?......?|?......?|
    |----known-----||--m1---|

    cipher --> qspuapswoto4px8s != 892oaksm3ud2lk4n #salah
   
   # loop 2
       plain = 'a'*15 + b
    
    Block 1          Block 2  Block 3
    |aaaaaaaaaaaaaaab|?......?|?......?|
    |----known-----||--m1---|

    cipher --> voi73n95nyqxdlks != 892oaksm3ud2lk4n #salah

   # loop 3
       plain = 'a'*15 + b
    
    Block 1          Block 2  Block 3
    |aaaaaaaaaaaaaaac|?......?|?......?|
    |----known-----||--m1---|

    cipher --> 892oaksm3ud2lk4n == 892oaksm3ud2lk4n #benar
 
    #kita dapatkan bahwa "?" dalam "aaaaaaaaaaaaaaa?" adalah "c".
   ```
   
4. Ulangi proses tersebut hingga karakter pertama dalam blok juga ditemukan.
    ```
    # loop 1

    Block 1          Block 2  Block 3
    |aaaaaaaaaaaaaac?|?......?|?......?|
    |----known-----||--m1---|

    # loop 2 
    # (ditemukan karakter selanjutnya adalah o)
    
    Block 1          Block 2  Block 3
    |aaaaaaaaaaaaaco?|?......?|?......?|
    |----known-----||--m1---|

    # loop 3 
    # (ditemukan karakter selanjutnya adalah m)

    Block 1          Block 2  Block 3
    |aaaaaaaaaaaacom?|?......?|?......?|
    |----known-----||--m1---|

    ...
    # loop 16
    Block 1          Block 2  Block 3
    |compfest14{indep|?......?|?......?|
    |----known-----||--m1---|
   ```

5. Untuk blok selanjutnya, kita harus mengencrypt 15 known plaintext juga dengan membandingkan blok yang diinginkan.
   ```
    # cipher hasil block 2 di sini sebagai acuan
    Block 1               Block 2       Block 3
    |aaaaaaaaaaaaaaac|ompfest14{indep?|?......?|
    |---------------known-----------||--m2---|

    # cipher hasil block 2 di sini sebagai oracle
    Block 1                 Block 2         Block 3
    |aaaaaaaaaaaaaaac|ompfest14{indepB|compfest14{indep|
    |----kontrol---||-----plain-----|^brute

   ```