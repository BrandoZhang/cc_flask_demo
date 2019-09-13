## Introduction
This is a simple dockerized flask demo used in CSC4160/CIE6129@CUHKSZ.

## Set-up
Make sure you've installed and started docker service.

```bash
docker pull brandoz/cc_flask_demo
docker run -d --name cc_flask -p 5000:5000 brandoz/cc_flask_demo
```

## Acknowledge
Modified from [sjeeva/flaskapp](https://github.com/sjeeva/flaskapp)