#!/bin/sh

tshark -ni any -w output.pcap &
python3 /root/echoserv.py &
python3 pp.py
