CC=gcc
FLAGS=-fPIE -pie -z relro -z now -fno-stack-protector
TARGET=pibolar
OBJS=source.c

all: $(OBJS)
	$(CC) $(FLAGS) $(OBJS) -o $(TARGET)