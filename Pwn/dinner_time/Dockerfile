FROM ubuntu:16.04
MAINTAINER Sai Vegasena

#installation
RUN apt-get update && apt-get install -y \
    apt-utils \
    build-essential \
    socat

#user

RUN useradd -ms /bin/sh dinner
WORKDIR /home/dinner

COPY ./art.txt ./
COPY ./dinner ./
COPY ./run.sh ./
COPY ./flag.txt ./

RUN chown -R root:dinner /home/dinner && \
     chmod 750 /home/dinner && \
     chown root:dinner /home/dinner/flag.txt && \
     chmod 440 /home/dinner/flag.txt && \
     chmod 550 /home/dinner/run.sh && \
	 chmod 550 /home/dinner/dinner && \
     chmod 550 /home/dinner/art.txt


EXPOSE 1345

CMD ["socat", "-T60", "TCP-LISTEN:1345,reuseaddr,fork,su=dinner","EXEC:/home/dinner/run.sh,pty"]
