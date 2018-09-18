CC=gcc
FLAGS=-z relro -z now -fno-stack-protector
TARGET=adhd
OBJS=source.c

all: $(OBJS)
	$(CC) $(FLAGS) $(OBJS) -o $(TARGET)