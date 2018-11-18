#!/bin/sh

tshark -ni any -w output.pcap &
python3 /root/server.py &
python3 /root/ticker/main.py &

sleep 5
echo "moving forward"
python3 /root/tbp.py &
wait
