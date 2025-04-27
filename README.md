# Simple REST API with Fast API

## Required software

- [mise](https://github.com/jdx/mise)
- [docker](https://www.docker.com/ja-jp/)

## How to execute

1. Set up GitHub repository

```shell
git clone https://github.com/ohashih/simple-rest-api.git && \
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

Access to when lancher API server `http://localhost:8000/docs`
