# Writeup The Maze Jogger
Diberikan suatu maze persegi yang terdiri atas n x n cell, dengan n bilangan acak dari 20 hingga 25. Kita tidak bisa melihat apa-apa kecuali koordinat kita, jarak dari tujuan, dan apakah bisa bergerak ke depan/belakang/kiri/kanan.

Dari informasi koordinat kita, kita dapat menyimpan setiap cell sebagai object node dalam graph. Pengecekan neighbors untuk setiap node dilakukan dengan mencoba melangkah ke setiap arah, dan menyimpan setiap cell yang dapat didatangi dari cell saat ini.

Lalu, kita dapat menerapkan algo pathfinding sesuai dengan keinginan kita, pada solver terlampir digunakan greedy best first search. Kita juga perlu menyimpan path terpendek untuk mencapai suatu cell (dua arah), agar dapat backtracking apabila terdapat sel yang heuristic valuenya lebih menjanjikan.