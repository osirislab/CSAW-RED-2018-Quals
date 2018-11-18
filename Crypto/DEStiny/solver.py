from Crypto.Cipher import DES
import binascii

key = binascii.unhexlify('1F1F1F1F0E0E0E0E')
iv = '66642069'
enc = open('destiny.enc').read()
cipher = DES.new(key, DES.MODE_OFB, iv)
msg = cipher.decrypt(enc[8:])
print msg
