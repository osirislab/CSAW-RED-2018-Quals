FROM mysql:8
MAINTAINER John Cunniff

ENV NAME BlindAsABat
ENV PORT 1234

ENV MYSQL_USER red_user
ENV MYSQL_PASSWORD password
ENV MYSQL_DATABASE the_db_you_are_looking_for
ENV MYSQL_ROOT_PASSWORD password

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install gunicorn Flask pymysql

COPY init_db.sql /docker-entrypoint-initdb.d/
COPY start.sh /docker-entrypoint-initdb.d/

WORKDIR /${NAME}
COPY . /${NAME}
