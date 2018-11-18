FROM ubuntu:16.04
MAINTAINER Sai Vegasena

#installation
RUN apt-get update && apt-get install -y \
    apt-utils \
    build-essential \
    socat

#user

RUN useradd -ms /bin/sh got
WORKDIR /home/got

COPY ./art.txt ./
COPY ./got ./
COPY ./run.sh ./
COPY ./flag.txt ./

RUN chown -R root:got /home/got && \
     chmod 750 /home/got && \
     chown root:got /home/got/flag.txt && \
     chmod 440 /home/got/flag.txt && \
     chmod 550 /home/got/run.sh && \
	 chmod 550 /home/got/got && \
     chmod 550 /home/got/art.txt


EXPOSE 1436

CMD ["socat", "-T60", "TCP-LISTEN:1436,reuseaddr,fork,su=got","EXEC:/home/got/run.sh,pty"]
