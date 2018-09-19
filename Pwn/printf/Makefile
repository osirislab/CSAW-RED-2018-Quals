CC=gcc
FLAGS=-fPIE -pie -z relro -z now
TARGET=pf
OBJS=source.c

all: $(OBJS)
	$(CC) $(FLAGS) $(OBJS) -o $(TARGET)