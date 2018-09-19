#!/usr/bin/env python3.6

#print out SSA and user has to give ending value of each SSA object

from random import randint, choice, shuffle

class StateModel:
    def __init__(self):
        self.ins = 1
        self.ssa_var_vals = {"%0":1337}

class Value:
    def __init__(self, name, vtype):
        self.name, self.type = name, vtype

ops = [
    "add",
    "sub",
    "rshift",
    "lshift",
    "mult",
    "xor" ,
    "and",
    "or",
]

spec_ops = [
    "showitem"
]

def generate_iformat(smodel):
    ins = choice(ops)
    
    if len(smodel.ssa_var_vals) == 0:
        op1 = "%0"
    else:
        op1 = choice(list(smodel.ssa_var_vals.keys()))
    
    imm = randint(0, 100)
    ins = f"%{smodel.ins} = {ins} {op1}, {imm}"
    print(ins)
    smodel.ssa_var_vals["%" + str(smodel.ins)] = ins
    smodel.ins += 1

def generate_rformat(smodel):
    ins = choice(ops)
    
    if len(smodel.ssa_var_vals) == 0:
        op1 = "%0"
    else:
        op1 = choice(list(smodel.ssa_var_vals.keys()))
    
    if len(smodel.ssa_var_vals) == 0:
        op2 = "%0"
    else:
        op2 = choice(list(smodel.ssa_var_vals.keys()))
    
    ins = f"%{smodel.ins} = {ins} {op1}, {op2}"
    print(ins)
    smodel.ssa_var_vals["%" + str(smodel.ins)] = ins
    smodel.ins += 1

def validate(state_model):
    pass

def generate_code():
    state_model = StateModel()
    ins = []
    icount = randint(10,19)

    print(f"%0 = 0x{randint(123456,654321)}")
    for i in range(icount):
        generate_iformat(state_model) 
        generate_rformat(state_model) 

    keys = list(state_model.ssa_var_vals.keys())
    last = keys[-1]
    shuffle(keys)
    print(f"show {keys.pop()} + {keys.pop()} + {keys.pop()} + {keys.pop()} + {keys.pop()} + {keys.pop()} + {last}")
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
    print("\t%0 = 0x158763\n\t%1 = 0\n%2=-1410915")
    print("Show instruction outputs:   0")
    print("*" * 75)

def print_flag():
    with open("flag.txt") as flag:
        print(flag.read())

if __name__ == "__main__":
    instructions()
    for i in range(1):
        solution = generate_code()
        try:
            res = float(input("What does the program output??: "))
        except:
            print("HEEEEYY THAT ISN'T VALID INPUT FORMAT!")
            exit()
        if abs(res - solution) <= 1:
            print("YAAAY KEEEP GOING !!")
        else:
            print("NOO! TRY AGAIN (:")

    print_flag()

