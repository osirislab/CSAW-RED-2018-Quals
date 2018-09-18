#!/usr/bin/env python
from pwn import *
sol = "csawRedFtw!"
p = process("./chary")
p.recvuntil(":")
p.sendline(sol)
print p.recvall()
