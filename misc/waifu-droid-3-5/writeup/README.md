# Writeup - WaifuDroid 3

Diberikan suatu bot Discord. Kita perlu melakukan code golf pada suatu set karakter yang mirip JSFuck, tetapi lebih restriktif. Kita dapat menggunakan berbagai trik coercion pada JavaScript dengan referensi berikut.
https://codegolf.stackexchange.com/questions/198472/wtf-js-obfuscator

Ide dasarnya adalah seperti ini.
```js
+[] // 0
~[] // -1
-~[] // 1
![] // false
![]+[] // 'false'
[![]+[]] // ['false']
[![]+[]][+[]] // 'false' (kenapa pakai ini? Supaya bisa ambil salah satu karakternya)
[![]+[]][+[]][+[]] // 'f'
[![]+[]][+[]][-~[]] // 'a'
[![]+[]][+[]][-~[]-~[]] // 'l'
```
dst.

Untuk mendapatkan karakter selain dari yang teroptimisasi tersebut, kita dapat melakukan ekspansi lagi. Berikut referensi yang bisa dipakai (peserta mungkin perlu mengoptimisasi lagi dari referensi tersebut).
https://stackoverflow.com/questions/63673610/alternative-way-to-get-c-letter-in-jsfuck

Soal ini idealnya tidak dapat dikerjakan hanya dengan bantuan tools (yang ada di internet, meskipun link [ini](https://github.com/centime/jsfsck) cukup optimised tetapi tidak cukup), peserta perlu mengoptimisasi sendiri dari berbagai teknik encoding JSFuck yang ada. Karakter set yang digunakan juga lebih restriktif daripada JSFuck pada umumnya.
Solusi dari soal ini terdapat pada `payload.txt` dan penjelasannya pada `payload_breakdown.txt`

## Flag
```
COMPFEST14{w0w_jS_iS_s0_we1rD_HuH_s3r10u5lY_w0t_wos_dat_d0baa4f9d0}
```