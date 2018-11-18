"""
We got an awesome new take on the visionair cipher that iterates over a key in order to encrypt/decrypt flags. Basically we iterate over a key for a length _l_ and encrypt the plaintext using that chunk of the key. The ciphertext is made up of chunks of size _l_ of each individual cipher. The cipher text is `fmcj{aj_rzxn_mpxc_knwxabb}`. Use the flag format to your advantage in cracking the code.
"""
import re
import string

alphabets = "abcdefghijklmnopqrstuvwxyz" 
def encrypt(p, k):
    c = ""
    kpos = []
    for x in k:
        if x in alphabets:
            kpos.append(alphabets.find(x))
    i = 0
    for x in p:
        if x in alphabets:
          if i == len(kpos):
              i = 0
          pos = alphabets.find(x) + kpos[i] 
          if pos > 25:
              pos = pos-26               
          c += alphabets[pos]  
          i +=1
        else:
            c += x
    return c

def decrypt(c, k):
    p = ""
    kpos = []
    for x in k:
        if x in alphabets:
            kpos.append(alphabets.find(x))
    i = 0
    for x in c:
        if x in alphabets:
          if i == len(kpos):
              i = 0
          pos = alphabets.find(x.lower()) - kpos[i]
          if pos < 0:
              pos = pos + 26
          p += alphabets[pos].lower()
          i +=1
        else:
          p += x
    return p


print "Iterative Vision Air\n"

p = "flag{we_hope_yall_succeed}"

c = ""
for i in range(0, 26, 4):
    temp = encrypt(p, alphabets[i:i+4])
    c += temp[i:i+4]

print "The cipher text is: ", c

p = ""
for i in range(0, 26, 4):
    temp = decrypt(c, alphabets[i:i+4])
    p += temp[i:i+4]

print "The plain  text is: ", p

partial = decrypt(c, "flag")[:4]
print "The partial key is: ", partial
print "Part plain text is: ", decrypt(c, partial)
print "Part plain text is: ", decrypt(c, "efgh")
print "Part plain text is: ", decrypt(c, "ijkl")
print "Part plain text is: ", decrypt(c, "mnop")
print "Part plain text is: ", decrypt(c, "qrst")
print "Part plain text is: ", decrypt(c, "uvwx")
print "Part plain text is: ", decrypt(c, "yz")

