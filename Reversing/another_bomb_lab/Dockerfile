FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    apt-utils \
    build-essential \
    socat


RUN useradd -ms /bin/sh bomb
WORKDIR /home/bomb

COPY flag.txt ./
COPY bomb.c ./
COPY Makefile ./

RUN make
RUN chown -R root:bomb /home/bomb && \
    chmod 750 /home/bomb && \
    chown root:bomb /home/bomb/flag.txt && \
    chmod 440 /home/bomb/flag.txt && \
    chmod 550 /home/bomb/bomb

EXPOSE 9898
CMD ["socat", "-T60", "TCP-LISTEN:9898,reuseaddr,fork,su=bomb", "EXEC:/home/bomb/bomb,pty"]
