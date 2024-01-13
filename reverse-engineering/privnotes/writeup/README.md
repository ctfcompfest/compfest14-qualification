# Writeup PrivNotes
Diberikan suatu file .apk yang cukup besar. Bisa langsung diekspor saja dengan tool semacam `apktool`.

```
apktool d privnote.apk
```

![img1](https://cdn.discordapp.com/attachments/815844122673938453/1007670890173050880/unknown.png)

![img2](https://cdn.discordapp.com/attachments/815844122673938453/1007670969969680404/unknown.png)

Berdasarkan struktur direktorinya, kita menemukan bahwa program tersebut menggunakan Flutter, dan terdapat file `kernel_blob.bin` pada `assets/flutter_assets` yang menandakan bahwa apk tersebut di-build dalam debug mode, sehingga kita dapat langsung me-leak source code aslinya.

![img3](https://cdn.discordapp.com/attachments/815844122673938453/1007671464884961309/unknown.png)

Dari file keluaran tersebut, kita dapat melihat source code dari aplikasi, dan ternyata program tersebut melakukan XOR input terhadap kedua isi note yang telah hardcoded, kemudian membandingkannya terhadap suatu array bytes. Pengecekan berhenti apabila password telah mencapai karakter '}'.

![img4](https://cdn.discordapp.com/attachments/815844122673938453/1007673348295249981/unknown.png)

Sehingga, kita dapat melakukan bruteforcing dari 0-128 untuk setiap karakternya, dan berhenti ketika telah mencapai karakter '}'.

![img5](https://cdn.discordapp.com/attachments/815844122673938453/1007672575167569990/unknown.png)