#all this does is query the IP, just writing this so that it's automatic once everything is set up

import requests

ip_addr = "" #to be determined once we have something registered

r = requests.get(ip_addr)
