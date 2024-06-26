# Theatre API Service:

API service for theatre management written on DRF

## Installing using GitHub

* Install PostgreSQL and create db
* Python3 must be already installed

```shell
git clone https://github.com/pnasonov/theatre-api-service
cd theatre-api-service

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

set DJANGO_SECRET_KEY=<your django secret key>
set POSTGRES_DB=<your db name>
set POSTGRES_USER=<your db username>
set POSTGRES_PASSWORD=<your db user password>
set POSTGRES_HOST=<your db hostname>
set POSTGRES_PORT=<your db port>
set POSTGRES_DATA=/var/lib/postgresql/data

python manage.py migrate
python manage.py runserver
```

## Run with docker

* Docker should be installed

```shell
docker-compose build
docker-compose up
```

## Getting access

* create user via /api/user/register/
* get access token via /api/user/token/
