FROM ubuntu:18.04
MAINTAINER John Cunniff

ENV NAME=SQLIntro
ENV PORT=1234

RUN apt-get update
RUN apt-get install -y python3.6 python3-pip
RUN pip3 install gunicorn Flask

WORKDIR /${NAME}
COPY . /${NAME}

RUN python3 /${NAME}/db.py --init

EXPOSE ${PORT}

CMD gunicorn -b 0.0.0.0:${PORT} -w 8 app:app 0.0.0.0 ${PORT}
