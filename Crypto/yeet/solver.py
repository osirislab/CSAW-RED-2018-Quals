from base64 import b64decode

with open('ciphertext.txt', 'r') as f:
  enc = b64decode(f.read())

  for i in range(0, 255):

    decoded = []

    for c in enc:
      d = ord(c) ^ i
      decoded.append(chr(d))
    
    decoded = ''.join(decoded)
    if 'flag' in decoded:
      print(decoded)
      exit()