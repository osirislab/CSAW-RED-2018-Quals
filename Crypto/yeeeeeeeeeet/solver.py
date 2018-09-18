from base64 import b64decode
from itertools import cycle

def num_to_key(n):

  key = []

  while n > 255:
    key.append(255)
    n = n // 255
  
  key.append(n)
  return reversed(key)


with open('ciphertext.txt', 'r') as f:
  enc = b64decode(f.read())

  for i in xrange(1, 0xffffffff):
    
    k = cycle(num_to_key(i))
    k = cycle(map(ord, 'yeet')) # just to save time. You can run it if you'd like, but it takes quite a while
    decoded = []

    for c in enc:
      d = ord(c) ^ next(k)
      decoded.append(chr(d))
    
    decoded = ''.join(decoded)
    print '\r' + hex(i),
    if 'flag' in decoded:
      print(decoded)
      exit()