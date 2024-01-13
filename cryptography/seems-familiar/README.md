# Seems Familiar

by houseoforion

---

## Flag

```
COMPFEST14{1nDeP3ndenT_bLoCK_ENCryPt10n_w1Th_fl4G_ApP3nDED_0f_course_iTS_eCB_oracLE_f97ae3a047}
```

## Description
Your friend has developed an AES-based enryption system in his spare time. That system is very limited and only able to use printable characters, and furthermore, two of four of its functions has yet to be fixed. Even though they are broken, he insisted the flag can be acquired through thorough analysis of the encryption itself. Feeling intrigued, you feel like you are able to get the flag.

## Difficulty
easy-medium

## Hints
* I wonder what happens if you give empty string as a plaintext. . .

## Tags
AES, ECB, Oracle Attack, Known Plaintext Attack

## Deployment

- Install docker engine>=20.10.17 and docker-compose>=1.29.2
- Run the container using:
    ```
    docker-compose up --build --detach
    ```


## Notes
Perlu stress-test karena perlu bruteforcing dalam known plaintext attack. Jika brutefore menggunakan python string.printables, flag didapatkan dalam sekitar 5349 request. 
