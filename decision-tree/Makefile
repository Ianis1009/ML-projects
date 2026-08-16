CC = gcc

CFLAGS = -Wall -Wextra -std=c11 -O2

TARGET = decision_tree

SRC = main.c tree.c

all:
	$(CC) $(CFLAGS) $(SRC) -o $(TARGET)


run: all
	./$(TARGET)


clean:
	rm -f $(TARGET)