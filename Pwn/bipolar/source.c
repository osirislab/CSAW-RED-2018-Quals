#include <stdio.h>
#include <unistd.h>

void print_flag() {
  FILE* f = fopen("flag.txt", "r");
  char buf[255];
  fgets(buf, 255, f);

  printf("%s\n", buf);
}

void get_input() {
  char buf[0x8];

  read(0, buf, 0x20);
}

int main() {
  printf("Hello Kyle. How are you doing today?\n");
  get_input();
}