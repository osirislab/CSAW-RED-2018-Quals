#!/usr/bin/env python
from pwn import *
p = process("./run.sh")
p.recvuntil("??")
p.sendline("csawaaaaaaaawasc")
print p.recvall()
