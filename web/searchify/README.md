# Searchify

Sui

---

## Flag

```
COMPFEST14{wh00ps_it5_n0t_s3cure_after_4ll_9b59fcb913}
```

## Description
> I won't do anything unnecessary. It's just a low-key search engine clone, so bugs are expected.

```
http://<ip>:9013
```

## Difficulty
Tingkat kesulitan soal: medium/hard (?)

## Hints
* It was affected by a common exploit back in 2021. But I don't have a time to upgrade the webserver. Therefore, I patch it with a certain WAF rule

## Tags
web, waf

## Deployment
**Build & run the container**
```bash
$ docker-compose  up -d --build
```

**Stop the container**
```bash
$ docker-compose down
```

**Monitoring the container logs**
```bash
$ docker-compose logs

# or use ctop instead
# https://github.com/bcicen/ctop
$ ctop
```

## Notes
intentionally left empty

