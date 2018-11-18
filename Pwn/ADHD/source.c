#include <unistd.h>
#include <stdio.h>

int main() {
  printf("Give give:\n");

  char buf[0x8];
  read(0, buf, 0x32);

  asm (
    "xor %rax, %rax\n"
    "xor %rdi, %rdi\n"
    "xor %rbx, %rbx\n"
    "xor %rcx, %rcx\n"
    "xor %edx, %edx\n"
    "xor %rsi, %rsi\n"
    "ret\n"
  );
}
