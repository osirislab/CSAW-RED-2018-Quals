#!/usr/bin/env python3.6

#print out SSA and user has to give ending value of each SSA object

from random import randint, choice

class StateModel:
    def __init__(self):
        self.ins = 1
        self.allocations = []
        self.ssa_var_vals = {"%0":1337}
        self.BB = []

class Value:
    def __init__(self, name, vtype):
        self.name, self.type = name, vtype

branch_ops = [
    "breq",
    "jmp"
]

mem_ops = [
    "store",
    "allocate",
    "load"
]

cmp_ops = [
    "icmp"
]

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


def generate_branch(smodel):
    pass

def generate_allocate(smodel):
    pass

def generate_store(smodel):
    pass

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
    
def generate_code():
    state_model = StateModel()
    ins = []
    icount = randint(2,5)

    for i in range(randint(1,4)):
        generate_allocate(state_model)


    for i in range(icount):
        #print(state_model.ssa_var_vals)
        generate_iformat(state_model)
        generate_rformat(state_model)

    return ins

generate_code()
