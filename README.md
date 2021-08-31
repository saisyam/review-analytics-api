# Review Analytics
Building an application to analyze reviews using FastAPI, PostgreSQL and ReactJS.

## Run the application

```shell
$ python3 app/main.py
```

## Run PostgreSQL as docker
I am using `postgreSQL` docker for this application. You can run the docker using the following command:
```shell
$ docker run -e POSTGRES_PASSWORD=<Postgres password> -d postgres
```
The above command will download and run the `postgres:latest` docker image.
