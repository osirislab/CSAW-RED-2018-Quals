CC=gcc
FLAGS=-z relro -z now -fPIE -pie
TARGET=tic-tac-toe
OBJS=source.c

all: $(OBJS)
	$(CC) $(FLAGS) $(OBJS) -o $(TARGET)