#!/usr/bin/env python3.6
#print out SSA and user has to give ending value of each SSA object
from random import randint, choice, shuffle
from collections import defaultdict
import operator

ops = {
    "add": operator.add,
    "sub": operator.sub,
    "mult": operator.mul,
    "xor": operator.xor,
    "and": operator.and_,
    "or": operator.or_
}

class StateModel:
    def __init__(self):
        self.ins = 1
        self.ssa_var_vals = {"%0":None}

class Value:
    def __init__(self, name, vtype):
        self.name, self.type = name, vtype

def generate_iformat(smodel):
    ins = choice(list(ops.keys()))
    
    if len(smodel.ssa_var_vals) == 0:
        op1 = "%0"
    else:
        op1 = choice(list(smodel.ssa_var_vals.keys()))
    
    imm = randint(0, 7)
    ins = f">%{smodel.ins} = {ins} {op1}, {imm}"
    print(ins)
    smodel.ssa_var_vals["%" + str(smodel.ins)] = ins
    smodel.ins += 1

def generate_rformat(smodel):
    ins = choice(list(ops.keys()))
    
    if len(smodel.ssa_var_vals) == 0:
        op1 = "%0"
    else:
        op1 = choice(list(smodel.ssa_var_vals.keys()))
    
    if len(smodel.ssa_var_vals) == 0:
        op2 = "%0"
    else:
        op2 = choice(list(smodel.ssa_var_vals.keys()))
    
    ins = f">%{smodel.ins} = {ins} {op1}, {op2}"
    print(ins)
    smodel.ssa_var_vals["%" + str(smodel.ins)] = ins
    smodel.ins += 1

def validate(state_model):
    vals = defaultdict(int)
    for k,v in state_model.ssa_var_vals.items():
        if k == "%0":
            k,equ = v.split(" = ")
            vals[k.strip(">")] = int(equ, 16)
        elif k == "show":
            q = v.split(" ")
            total = 0
            for i in range(1,len(q),2):
                total += vals[q[i]]
        else:
            k, equ = v.split(" = ")
            oper, op1, op2 = equ.split(" ")
            op1 = op1.strip(",")

            if not op1.isdigit():
                op1 = vals[op1]
            else:
                op1 = int(op1)

            if not op2.isdigit():
                op2 = vals[op2]
            else:
                op2 = int(op2)

            vals[k.strip(">")] = ops[oper](op1, op2)
    return total

def generate_code():
    state_model = StateModel()
    ins = []
    icount = randint(10,14)

    state_model.ssa_var_vals["%0"] = f">%0 = 0x{randint(13,65)}"
    print(state_model.ssa_var_vals["%0"]) 
    for i in range(icount):
        generate_iformat(state_model) 
        generate_rformat(state_model) 

    keys = list(state_model.ssa_var_vals.keys())
    last = keys[-1]
    shuffle(keys)
    state_model.ssa_var_vals["show"]  = f">show {keys.pop()} + {keys.pop()} + {keys.pop()} + {keys.pop()} + {keys.pop()} + {keys.pop()} + {last}"
    print(state_model.ssa_var_vals["show"])
    solution = validate(state_model)
    return solution

def instructions():
    print("*" * 75)
    print("Your job is to write a simple program that executes instructions!")
    print("Each instruction is in the following format:")
    print("Value = op1 operand op2")
    print("A given Value stores the result of an instruction\n")
    print("Ex: ")
    print("%0 = 0x158763 # All programs start this way setting %0 to a hex number")
    print("%1 = rshift %0, 67 #\t%1 = %0 >> 67")
    print("%2 = sub %1, %0 #\t%2 = %1 - %0")
    print("show %0 + %1 + %2#\t You must submit the result of the show command\n")
    print("The show command is the output of the program")
    print("It is basically the sum of a subset of Values from the program\n")
    print("Since: ")
    print("\t%0 = 0x158763\n\t%1 = 0\n\t%2=-1410915")
    print("Show instruction outputs:   0")
    print("*" * 75)

def print_flag():
    with open("flag.txt") as flag:
        print(flag.read())

if __name__ == "__main__":
    instructions()
    for i in range(100):
        solution = generate_code()
        try:
            res = int(input("What does the program output??: "))
        except:
            print("HEEEEYY THAT ISN'T VALID INPUT FORMAT!")
            exit()
        if abs(res - solution) <= 100:
            print(res)
            print(solution)
            print("YAAAY KEEEP GOING !!")
        else:
            print("NOO! TRY AGAIN (:")
            exit()
        print("*" * 75)

    print_flag()
