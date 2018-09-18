#include <stdio.h>

const char * dessert = "/bin/sh";

int entree_1() {
    __asm__ volatile("syscall ; ret");
}

int entree_2() {
    __asm__ volatile("pop %rdi ; ret");
}

int entree_3() {
    __asm__ volatile("pop %rsi ; ret");
}

int entree_4() {
    __asm__ volatile("pop %rdx ; ret");
}

int entree_5() {
    __asm__ volatile("pop %rax ; ret");
}

int main() {
    char buf[0x30];
    puts("What will you be having for dinner !! (: \n");
    fgets(buf, 0x400, stdin);
    return 0;
}
