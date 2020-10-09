FROM python:3.8

WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
# COPY . .

RUN apt-get update && apt-get install -y wget

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
# This is a special case. We need to run this script as an entry point:
COPY ./docker/backend/docker_check_db.sh ./docker/backend/docker_runserver.sh /
RUN chmod +x /docker_check_db.sh /docker_runserver.sh

ENTRYPOINT ["/docker_check_db.sh"]