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


CHALLENGE 2
-----------

Oh no! Someone messed with the permutations of ingrediants and now I have no clue how to decipher the message! Try and recover the plaintext, well I mean do or do not there is no try so definitely recover the plaintext. 

'''

ingrediants = ['ROMAINE', 'DRESSING', 'ANCHOVIES', 'CROUTONS', 'PARMESAN']

def substitute(alphabet, substitute):
    x = substitute + alphabet
    y = []
    for a in x:
        if a not in y:
            y.append(a)
    return ''.join(y)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'
cipher = alphabet
plaintext = 'FLAG{I_LIKE_MY_SALAD_WITH_ANCHOVIES_THATS_HOW_CAESAR_INTENDED_IT}'

for item in ingrediants:
    cipher = substitute(cipher, item)
print("CHALLENGE PT 1\n" + "-"*20)
print("\nCipher: " + cipher)

def encrypt(plaintext, key, alphabet):
    keyIndices = [alphabet.index(k) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

def decrypt(cipher, key, alphabet):
    keyIndices = [key.index(k) for k in cipher]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)

ciphertext = encrypt(plaintext, cipher, alphabet)
print("Ciphertext: " + ciphertext)
print("Decrypted Plaintext: " + decrypt(ciphertext, cipher, alphabet))


print("\n\nCHALLENGE PT 2\n" + "-"*20 + "\n")

ingrediants_master_key = ['DRESSING', 'ANCHOVIES', 'PARMESAN', 'CROUTONS', 'ROMAINE']

print "Master Permutation:",
print(ingrediants_master_key)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'
cipher = alphabet
plaintext = 'FLAG{DRESSING_FIRST_IS_INSANITY_THE_ROMAINE_WONT_BE_PROPERLY_DRESSED}'

for item in ingrediants_master_key:
    cipher = substitute(cipher, item)

print("\nCipher: " + cipher)
ciphertext = encrypt(plaintext, cipher, alphabet)
print("Ciphertext: " + ciphertext)
print("Decrypted Plaintext: " + decrypt(ciphertext, cipher, alphabet))

print("\n\nCHALLENGE PT 2 SOLVER\n" + "-"*20 + "\n")

print("We are given the following: ")
print("Alphabet: " + alphabet)
print("Ciphertext: " + ciphertext)
print "Ingrediants:",
print ingrediants

from itertools import permutations

def solver():
    print "\nRunning Solver..."
    potential_flags = []
    for perm in permutations(ingrediants):
        cipher = alphabet
        for item in perm:
            cipher = substitute(cipher, item)
        plaintext = decrypt(ciphertext, cipher, alphabet)
        if "FLAG" in plaintext:
            potential_flags.append(plaintext)
    print "\nPotential Flags:"
    print "\n".join(potential_flags)

solver()
