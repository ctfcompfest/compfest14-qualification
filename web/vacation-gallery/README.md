# Vacation Gallery

by sl0ck

---

## Flag

```
COMPFEST14{i_guess_n0t_but_heres_your_prize_anyway_8018a6e893}
```

## Description
My friend just came back from a vacation in the Austrian Alps, Munich, and Weimar. Check out her photos!

```
http://<ip>:<port>
```

**Note**: For this challenge, there is a special prize of points (half of the final challenge points) for writeups that contain the shortest payload that is shorter than the limit. If several payloads have the same (shortest) length, all will get the prize.

## Difficulty
Hard

## Hints
* how does one filter in jinja2 again?

## Tags
Web, SSTI, filtered SSTI

## Deployment
- Make sure you already install docker >= 19.03.13 and docker-compose >= 1.27.4.
- Command to run container:
    ```
    docker-compose up -d --build
    ```
- Command to stop container:
    ```
    docker-compose down
    ```

## Notes
> Intentionally left empty