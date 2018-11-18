CC=gcc
FLAGS=-z relro -z now
TARGET=adhd
OBJS=source.c

all: $(OBJS)
	$(CC) $(FLAGS) $(OBJS) -o $(TARGET)