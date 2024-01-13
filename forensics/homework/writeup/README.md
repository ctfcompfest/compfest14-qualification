# Writeup Homework

'Description
Felix is a student from University of Indonesia. He's having problems with his assignment dokumen
He said that he forgot the password and the dokumen might be corrupted, would you pls help him ?'

Pertama kita memperoleh file zip yang terproteksi dengan password. Berdasarkan deskripsi, diketahui bahwa pemilik file merupakanmahasiswa Universitas Indonesia sehingga kemungkinan password dari file tsb menggunakan bahasa Indonesia. mari kita coba menggunakan wordlist indonesia untuk membuka file tsb.

![crack_Assignment_11.zip](https://i.imgur.com/cDSOOeS.png)

Setelah membuka file zip, kita memperoleh sebuah dokumen yang diketahui berdasarkan desc bahwa itu merupakan PR yang telah dikerjakan oleh Felix, namun dokumen tsb bisa dibuka. hmmm apa yang dimaksud felix dengan corrupt yaa...,coba kita cek apa yang hilang/corrupt dari dokumen tsb, kita bisa gunakan origami framework

![Open_with_pdfsh](https://i.imgur.com/osra4kK.png)

Menurut pdfsh, terdapat 3 error pada file tsb. Tepatnya pada offset 0x7da7, 0xb57d, 0xb5c0 dimana 2 error pertama terjadi karena penulisan yang salah (ditulis dengan "=====...") dan error terakhir terjadi karena objek nomor 6 tidak dapat ditentukan

karena diketahui bahwa pdf tersebut hanya berisi gambar, mari kita coba buka file tsb dengan tool pdfimages

![open_with_pdfimages](https://i.imgur.com/MgN0yzz.png)

saat dibaca kita memperoleh petunjuk bahwa terdapat banyak karakter ilegal dan tipe dari XObject 'X6' keliru

berdasarkan analisis dari kedua tool tsb, diketahui bahwa terdapat 3 error pada file tsb, yaitu :

* 1. karakter ilegal '====...' pada offset 0x7da7 dan 0xb57d
* 2. objek nomor 6 tidak dapat ditentukan
* 3. tipe dari XObject 'x6' keliru

mari telusuri error tsb satu per satu

* Error 1

![error_1_clue_1](https://i.imgur.com/akrY2Bv.png)

Dari sini kita bisa melihat bahwa sepertinya ada manipulasi pada hex string file tsb yang diawali dan diakhiri dengan "=========", mari kita grep string tersebut

![error_1_clue_2](https://i.imgur.com/bgSKNLS.png)

kita memperoleh 4 clue, yaitu:

* 1. Width = 510
* 2. Height = 100
* 3. Remove Mask
* 4. Use RGB

mari simpan clue tsb dan lanjut menganalis error ke 2 menggunakan pdfstreamdumper

![clue](https://i.imgur.com/phQNPst.png)

kita memperoleh clue lain dari pdfstreamdumper terkait XObject dimana XObject 'X6' merefer ke object no.6 dan XObject 'X4' merefer ke object no.4 .

![objek_4](https://i.imgur.com/IJ6J8sp.png)

Berikut merupakan data stream dari objek no.4, objek tsb merupakan sebuah gambar. Sebelumnya kita memperoleh sebuah hint yang mengatakan bahwa document tsb hanya berisi 2 gambar, dimana kita bisa menggunakan gambar yang ada sbg refrensi untuk memulihkan gambar yang hilang. mungkin dpt diasumsikan bahwa gambar pada objek no.6 sudah dimanipulasi sehingga pdf reader tidak bisa membaca gambar tsb. Mungkin kita bisa menggunakan properti dari objek no.4 untuk memulihkan objek no.6. Mari buka hex editor untuk melihatnya

![hex_objek_4](https://i.imgur.com/6ohslNL.png)

Berikut merupakan hex dari objek 4, kita bisa memperoleh berbagai informasi terkait height, width, dsb

![hex_objek_6](https://i.imgur.com/LMoG2FT.png)

Berikut merupakan hex dari objek 6, berbeda dari objek 4 pada objek 6 kita tidak memperoleh detail sama sekali

mari kita coba copy-paste hex dari objek 4 ke objek 6

![update_obj_5_hex](https://i.imgur.com/9UUcGzr.png)


![dokumen](https://i.imgur.com/uaANqnl.png)

Setelah di-paste, kita bisa melihat gambar baru, namun sepertinya gambar tersebut bukan merupakan flagnya, mungkin kita bisa mengedit properti dari gambar kedua menggunakan 4 clue yang kita temukan sebelumnya

* 1. edit Width & Height

![hex_fix_1](https://i.imgur.com/sfDQ1f8.png)
![image_fix_1](https://i.imgur.com/FAe8G3w.png)

* 2. remove mask

Mungkin yang dimaksud dari clue ini adalah remove properti SMask pada objek 6

![hex_fix_2](https://i.imgur.com/qZqPVUo.png)
![image_fix_2](https://i.imgur.com/MiODGDz.png)

* 3. Use RGB

mungkin kita harus menggunakan mode RGB untuk melihat gambar

![hex_fix_3](https://i.imgur.com/CPCPpf9.png)
![fix_dokumen](https://i.imgur.com/cTCtxUa.png)


Berikut stream detail dan hex dari objek 6 :

![stream_obj_6_fix](https://i.imgur.com/U752SPa.png)
![hex_obj_6_fix](https://i.imgur.com/8HQDwni.png)

flag : COMPFEST14{Pls_f1x_1t_F3lix_2ee854b0d6}