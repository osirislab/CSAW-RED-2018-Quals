FROM ubuntu:16.04
MAINTAINER Sai Vegasena

#installation
RUN apt-get update && apt-get install -y \
    apt-utils \
    build-essential \
    socat

#user

RUN useradd -ms /bin/sh poprops
WORKDIR /home/poprops

COPY ./art.txt ./
COPY ./poprops ./
COPY ./run.sh ./
COPY ./flag.txt ./

RUN chown -R root:poprops /home/poprops && \
     chmod 750 /home/poprops && \
     chown root:poprops /home/poprops/flag.txt && \
     chmod 440 /home/poprops/flag.txt && \
     chmod 550 /home/poprops/run.sh && \
	 chmod 550 /home/poprops/poprops && \
     chmod 550 /home/poprops/art.txt


EXPOSE 1345

CMD ["socat", "-T60", "TCP-LISTEN:1345,reuseaddr,fork,su=poprops","EXEC:/home/poprops/run.sh,pty"]
