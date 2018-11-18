from base64 import b64encode
import random

yeet_byte = random.randint(0, 255) #  this is an inclusive range

yeet_byte = ord('y') # because haha XD so random

with open('flag.txt', 'r') as i, open('ciphertext.txt', 'w+') as o:
  encoded = []
  for c in i.read():
    enc = chr(ord(c) ^ yeet_byte)
    encoded.append(enc)
  
  o.write(b64encode(''.join(encoded)))

