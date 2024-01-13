# Judul Soal

by kilometer

---

## Flag

```
COMPFEST14{s3amUlat0r_v3ry_e4sy_63e2c19257}
```

## Description
My brother has a new hobby, making a game. Yesterday, he makes a cool game, named Seamulator. I try to playing it, after did 7 action, my fish price was $20,000. But I forgot which are the actions did I take. Can you find the flag?

## Difficulty
easy

## Hints
basic arithmetic operations

## Tags

## Deployment
Penjelasan cara menjalankan service yang dibutuhkan serta requirementsnya.

#### Contoh 1
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run the container using:
    ```
    docker-compose up --build --detach
    ```

#### Contoh 2
- How to compile:
    ```
    gcc soal.c -o soal -O2 -D\_FORTIFY\_SOURCE=2 -fstack-protector-all -Wl,-z,now,-z,relro -Wall -no-pie
    ```
- Jalankan:
    ```
    ./soal
    ```
- Workdir di `/home/compfest14`
- Gunakan libc 2.31 ketika sudah keluar. Alias Ubuntu 20.04.

## Notes
Tambahan informasi untuk soal, deployment, atau serangan yang mungkin terjadi pada service soal
