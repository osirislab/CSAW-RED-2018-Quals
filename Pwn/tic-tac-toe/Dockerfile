FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y socat

RUN useradd -ms /bin/sh kyle

WORKDIR /home/kyle

COPY ./flag.txt ./
COPY ./tic-tac-toe ./
RUN chown -R root:kyle /home/kyle && \
    chmod 750 /home/kyle && \
    chown root:kyle /home/kyle/flag.txt && \
    chmod 440 /home/kyle/flag.txt && \
    chmod 550 /home/kyle/tic-tac-toe

EXPOSE 8000

CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,fork,su=kyle", "EXEC:/home/kyle/tic-tac-toe,stderr,pty,rawer"]
