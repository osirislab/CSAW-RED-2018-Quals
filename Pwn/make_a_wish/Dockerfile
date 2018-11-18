FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y \
	apt-utils \ 
	build-essential \
	socat

RUN useradd -ms /bin/sh mina
WORKDIR /home/mina

COPY ./flag.txt ./
COPY ./b0f ./
COPY ./run.sh ./
RUN chown -R root:mina /home/mina && \
    chmod 750 /home/mina && \
    chown root:mina /home/mina/flag.txt && \
    chmod 440 /home/mina/flag.txt && \
    chmod 550 /home/mina/b0f && \
    chmod 550 /home/mina/run.sh 

EXPOSE 1337

CMD ["socat", "-T60", "TCP-LISTEN:1337,reuseaddr,fork,su=mina", "EXEC:/home/mina/run.sh,pty,rawer"]

