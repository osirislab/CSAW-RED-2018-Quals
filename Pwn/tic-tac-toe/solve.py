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

