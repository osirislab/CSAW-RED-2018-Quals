#!/usr/bin/env python
from pwn import *

goal = 48
board = [[j+i for i in range(5)] for j in range(5)]

for i in board: print(i)

path = ""

score = 0

x,y = 0,0

for i in range(5):
    score += board[4][i]  #adds values in last row 4 time 
    x += 1
    score += board[i][0] #goes down the first column down 4 times
    y += 1

score -= 4 # Accounts for counting board[4][4] twice

path = "DU" * (goal - score)
path += "DDDDRRRR"

x += 4
y += 4

print "PATH IS {}".format(path)

p = process("./run.sh")
p.sendline(path)
print(p.recvall())
