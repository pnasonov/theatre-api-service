FROM python:3.11.6-alpine3.18
LABEL maintainer="pavlonasonov@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV WAIT_VERSION 2.12.1
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

USER my_user
