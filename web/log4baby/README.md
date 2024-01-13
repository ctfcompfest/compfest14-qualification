# Log4baby

by sl0ck

---

## Flag

```
COMPFEST14{thats_your_log4j_chall_now_lets_save_the_planet_eee7d7c6ff}
```

## Description
Yes yes, I hear you say. What’s a 2022 CTF without a l4j challenge? Here’s one for babies.
Wrap the secret around `COMPFEST14{}` for the flag.

## Difficulty
medium

## Hints
* DNS lookups leave a trace you know….

## Tags
Log4shell, DNS Logging, CVE-2021-44228

## Deployment
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run the container using:
    ```
    docker-compose up --build --detach
    ```

## Notes
> Intentionally left empty