#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned long long uint64_t;
// typedef long long int64_t;

char board[3][3];

char EMPTY = 0x20;
char PLY1 = 'X'; // HOUSE ALWAYS WINS
char PLY2 = 'O'; // NERDS GO LAST

void print_board() {
  printf(
    " %c | %c | %c \n"
    "___|___|___\n"
    " %c | %c | %c \n" // remember that %c is one char
    "___|___|___\n"
    " %c | %c | %c \n",
    board[0][0], board[0][1], board[0][2],
    board[1][0], board[1][1], board[1][2],
    board[2][0], board[2][1], board[2][2]
  );
}

void new_board() {
  for (uint64_t y = 0; y < 3; ++y) {
    for (uint64_t x = 0; x < 3; ++x) {

      board[y][x] = 0x20; // Initialize board with space
    }
  }
}

void win(char c) {
  printf("%c wins!\n");
  exit(0);
}

void check_win(char c) {

  if ( 
    board[0][0] == c && board[0][1] == c && board[0][2] == c || // row 0
    board[1][0] == c && board[1][1] == c && board[2][2] == c || // row 1
    board[2][0] == c && board[2][1] == c && board[2][2] == c || // row 2
    board[0][0] == c && board[1][0] == c && board[2][0] == c || // col 0
    board[0][1] == c && board[1][1] == c && board[2][1] == c || // col 1
    board[0][2] == c && board[1][2] == c && board[2][2] == c || // col 2
    board[2][0] == c && board[1][1] == c && board[0][2] == c || // diag /
    board[0][0] == c && board[1][1] == c && board[2][2] == c // diag \

    ) // this space is because ^ that apparently skips the next line
  {
    win(c);
  }

}


void place(char c) {
  char buf[0x30];
  int64_t x, y;
  printf("Enter x:\n");

  fgets(buf, 0x30, stdin);

  x = atoll(buf);
  
  printf("Enter y:\n");
  fgets(buf, 0x30, stdin);

  y = atoll(buf);

  if (x >= 3 || y >= 3) {
    printf("Out of bounds. Please try again!\n");
    return;
  }

  if (board[y][x] != EMPTY) {
    printf("This space is not empty. Please try again!\n");
    return;
  }

  board[y][x] = c;
  print_board();

  check_win(c);
}

int main() {

  new_board();
  while (1) {
    printf("Player 1's turn\n");
    place(PLY1);
    printf("Player 2's turn\n");
    place(PLY2);
  }
}