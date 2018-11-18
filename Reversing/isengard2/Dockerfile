FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat python-dev python

RUN useradd -ms /bin/sh isengard2

WORKDIR /home/isengard2

ADD . ./
EXPOSE 8000

USER isengard2

CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,fork", "EXEC:/home/isengard2/checker.py,pty,stderr"]
