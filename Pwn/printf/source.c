#include <stdio.h>

void print_flag() {
  FILE* f = fopen("flag.txt", "r");
  char buf[255];
  fgets(buf, 255, f);

  printf("%s\n", buf);
}

void do_the_thing() {
  printf("Hello Kyle. How are you doing today?\n");

  char buf[0x30];
  fgets(buf, 0x30, stdin);

  printf(buf);

  printf("Next one:\n");

  fgets(buf, 0x30, stdin);

  printf(buf);
}

int main() {
  do_the_thing();
}