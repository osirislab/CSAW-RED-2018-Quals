#!/usr/bin/env python
from z3 import *
from pwn import *

p = process("./babyrev")

def gen_sol():
    with open("solve.txt", "r") as rands:
        x = rands.readlines()

        for i in x:
            s = Solver()
            a = BitVec('x', 32)
            n = int(i.strip())
            s.add((((a ^ (n % 100)) * 3) - 1) == 0x1337)
            s.check()
            model = s.model()
            yield [model[i] for i in model].pop()


p.recvuntil("???")
for i in gen_sol():
    p.sendline(str(i))
    p.recvn(len("YAAAY Keep GOING !!\n"))

print p.recvall()
