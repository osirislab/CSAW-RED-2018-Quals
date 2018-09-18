from base64 import b64encode
import random
from itertools import cycle

yeet_str = 'yeet'
chr_cycler = cycle(yeet_str)

with open('flag.txt', 'r') as i, open('ciphertext.txt', 'w+') as o:
  encoded = []
  for c in i.read():
    enc = chr(ord(c) ^ ord(next(chr_cycler)))
    encoded.append(enc)
  
  o.write(b64encode(''.join(encoded)))

