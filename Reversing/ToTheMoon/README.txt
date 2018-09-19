Working in blockchain you find only the best, most secure code. I bet you can't authenticate in my contract.

flag{WH4T_MONEY}

Give the bytecode and the abi files, release the sol file on the second day if there are no solves.

1) figure out how to reverse it (the name of the challenge is a hint to tooling)
2) figure out which function is a good target function - aka which has 'flag' in it
3) find the winning path in the function - when you pass in the right username it will print out something different
4) figure out what algo is used to hash the password (its SHA1)
5) recover the flag through brute forcing 4 characters in SHA1
6) submit the flag 
