import time
import requests
import urllib
import random

addrs = []

echo_addr = "http://127.0.0.1:5000/{}"

flag = ""

flagged = False
with open("urls", 'r') as urls:
    addrs = urls.read().split()

with open("flag", 'r') as flagfile:
    flag = list(flagfile.read())

flag = " ".join(flag)

for a in addrs:
    #time.sleep(random.randint(0,8))
    r = requests.get(a)
    payload = "" 
    if random.randint(0,4) == 2 and not flagged:
        payload = urllib.parse.urlencode({"result":flag})
        flagged = True
    else:
        payload = r.text
        payload = urllib.parse.urlencode({'result':payload[:180]})
    
    print(payload)
    x = requests.get(echo_addr.format(payload))
    print (x.text)
