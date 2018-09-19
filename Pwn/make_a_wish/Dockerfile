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
RUN chown -R root:mina /home/mina && \
    chown 750 /home/mina && \
    chown root:mina /home/mina/flag.txt && \
    chown 440 /home/mina/flag.txt && \
    chown 550 /home/mina/b0f 

EXPOSE 1337

CMD ["socat", "-T60", "TCP-LISTEN:1337,reuseaddr,fork,su=mina", "EXEC:/home/mina/b0f,pty,rawer"]

