from pwn import *

p = process("./bomb")
print p.recvline()
print p.recvline()
p.sendline('yadot_smoob_on')
print p.recvline()
p.sendline('163 99 67 44 38 23 21 15')
print p.recvline()
print p.recvline()
p.sendline('2297')
print p.recvline()