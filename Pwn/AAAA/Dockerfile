FROM ubuntu:16.04
MAINTAINER Sai Vegasena

#installation
RUN apt-get update && apt-get install -y \
    apt-utils \
    build-essential \
    socat

#user

RUN useradd -ms /bin/sh buff
WORKDIR /home/buff

COPY ./art.txt ./
COPY ./buff ./
COPY ./run.sh ./
COPY ./flag.txt ./

RUN chown -R root:buff /home/buff && \
     chmod 750 /home/buff && \
     chown root:buff /home/buff/flag.txt && \
     chmod 440 /home/buff/flag.txt && \
     chmod 550 /home/buff/run.sh && \
	 chmod 550 /home/buff/buff && \
     chmod 550 /home/buff/art.txt


EXPOSE 1436

CMD ["socat", "-T60", "TCP-LISTEN:1436,reuseaddr,fork,su=buff","EXEC:/home/buff/run.sh,pty"]
