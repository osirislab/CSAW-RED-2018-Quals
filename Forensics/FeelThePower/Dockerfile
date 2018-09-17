FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install iproute2 openssh-server -y

WORKDIR /data
COPY flagfile /data

