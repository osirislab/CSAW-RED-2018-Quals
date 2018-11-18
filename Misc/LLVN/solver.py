#!/usr/bin/env python
from pwn import *
from collections import defaultdict

p = process("./code_gen.py")
context.log_level = "debug"

p.recvuntil("*"*75)
p.recvuntil("*"*75)

ops = {
    "add": operator.add,
    "sub": operator.sub,
    "mult": operator.mul,
    "xor": operator.xor,
    "and": operator.and_,
    "or": operator.or_
}

while 1:
    vals = defaultdict(int)
    ins = p.recvuntil("??:")
    ins = [i.strip() for i in ins.split(">") if i != "\n"]

    for i in ins:
        try:
            k, v = i.split(" = ")
        except:
            k,v = "show", i.strip(" show") 
            pass

        if k.strip() == "%0":
            vals[k.strip()] = int(v, 16)
	    #print(vals[k])
        elif k == "show":
            total = 0
	    v = v[:-31].split(" ")
	    v = [x.strip() for x in v if x != "+"]
	    for i in v:
		total += vals[i]
	#	print(i,vals[i])
	    
	    p.sendline(str(total))
        else:
            oper, op1, op2 = v.split(" ")
            op1 = op1.strip(",")
	    
            if not op1.strip().isdigit():
                op1 = vals[op1.strip()]
            else:
                op1 = int(op1)
            if not op2.strip().isdigit():
                op2 = vals[op2.strip()]
            else:
                op2 = int(op2)
            #print(oper, op1, op2)
            vals[k.strip()] = ops[oper](op1, op2)
	    #print(vals[k.strip()])
    p.recvuntil("YAAAY KEEEP GOING !!")
    p.recvuntil("*"*75)
