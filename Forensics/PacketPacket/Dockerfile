FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install python3 python3-dev python3-pip  -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install tshark -y 

COPY . /root

WORKDIR /root
RUN pip3 install -r requirements.txt
RUN chmod +x start.sh
RUN touch output.pcap

CMD ./start.sh
