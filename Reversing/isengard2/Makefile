CC=gcc
CFLAGS=-pthread -s
RFLAGS=-ldl -lncurses -masm=intel


isengard2: main.c tree.c
	$(CC) $(CFLAGS) main.c tree.c $(RFLAGS) -o isengard2

flag_gen: gen.c tree.c
	$(CC)  gen.c tree.c -o gen
