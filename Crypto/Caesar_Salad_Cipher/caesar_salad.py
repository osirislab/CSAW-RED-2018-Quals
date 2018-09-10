# -*- coding: utf-8 -*-
'''
Caesar Salad Cipher - (Substitutions Are Extra)
-------------------
We all know the Caesar Cipher, but I've come up with a way more secure and delicious cipher system called the Caesar Salad Cipher. 

Items:

Anchovies
Croutons

Dressing
Parmesan
Romaine

Ciphers are cryptosystems where text -> cipher -> encrypted text -> cipher -> text aka they are reversible.

(3)   (4)
 A     C     
 N     R     
P A R M E S A N (5)
 C     O     
 H     U     
D R E S S I N G (2)
 O     T     
 V     O     
R O M A I N E (1)
 I     N     
 E     S     
 S           

A CDE GHI  LMNOP RSTUV   
 B   F   JK     Q     WXYZ

This _lettuce_ structure is a good representation of what makes a caesar salad and what makes a good cipher.

1. First Substitution: R O M A I N E

B: ABCDEFGHIJKLMNOPQRSTUVWXYZ
A: ROMAINEBCDFGHJKLPQSTUVWXYZ

2. Second Substitution: D R E S S I N G

B: ROMAINEBCDFGHJKLPQSTUVWXYZ
A: DRESINGOMABCFHJKLPQTUVWXYZ

3. Third Substitution: A N C H O V I E S

B: DRESINGOMABCFHJKLPQTUVWXYZ
A: ANCHOVIESDRGMBFJKLPQTUWXYZ

4. Fourth Substitution: C R O U T O N S

B: ANCHOVIESDRGMBFJKLPQTUWXYZ
A: CROUTNSAHVIEDGMBFJKLPQWXYZ

5. Fifth Substitution: P A R M E S A N

B: CROUTNSAHVIEDGMBFJKLPQWXYZ
A: PARMESNCOUTHVIDGBFJKLQWXYZ

It takes sometime to get the final substitution cipher used but thats pretty much it, it can be cracked fairly quickly but ¯\_(ツ)_/¯ high schoolers

CHALLENGE
---------

Give them the ingrediants and lettuce strucutre and the alphabet and the cipher and hopefully they take the substitution cipher hint and realize you need to "stack" the ingrediants onto the alphabet in lettuce strucutre order.

'''

ingrediants = ['ROMAINE', 'DRESSING', 'PARMESAN', 'ANCHOVIES', 'CROUTONS', 'PARMESAN']

def substitute(alphabet, substitute):
    x = substitute + alphabet
    y = []
    for a in x:
        if a not in y:
            y.append(a)
    return ''.join(y)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'
cipher = alphabet
plaintext = 'FLAG{YEET_TOO_LEET_CANT_BE_BEET}'

for item in ingrediants:
    cipher = substitute(cipher, item)
print(cipher)

def encrypt(plaintext, key, alphabet):
    keyIndices = [alphabet.index(k) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

def decrypt(cipher, key, alphabet):
    keyIndices = [key.index(k) for k in cipher]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)

ciphertext = encrypt(plaintext, cipher, alphabet)
print(ciphertext)
print(decrypt(ciphertext, cipher, alphabet))
