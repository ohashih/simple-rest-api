# Simple REST API with Fast API

## Table of contents

1. [Required software](https://github.com/ohashih/simple-rest-api?tab=readme-ov-file#required-software)
2. [How to execute](https://github.com/ohashih/simple-rest-api?tab=readme-ov-file#how-to-execute)
3. [API docs](https://github.com/ohashih/simple-rest-api?tab=readme-ov-file#api-docs)

## Required software

- [mise](https://github.com/jdx/mise)
- [docker](https://www.docker.com/ja-jp/)

## How to execute

1. Set up GitHub repository

```shell
git clone git@github.com:ohashih/simple-rest-api.git && \
    cd simple-rest-api
```

2. Install program language

```shell
mise trust && \
    mise install
```

3. Install modules with python

```shell
pip install --requirement requirements.txt
```

4. Launcher PostgreSQL on Docker

```shell
docker-compose up -d
```

5. Lancher API server

```shell
make run
```

## API docs

Access to `http://localhost:8000/docs` when lancher API server.
