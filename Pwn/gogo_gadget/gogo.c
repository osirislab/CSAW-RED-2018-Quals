#include <stdio.h>

const char * use_me = "/bin/sh";

int gadget_1() {
    __asm__ volatile("syscall ; ret");
}

int gadget_2() {
    __asm__ volatile("pop %rdi ; ret");
}

int gadget_3() {
    __asm__ volatile("pop %rsi ; ret");
}

int gadget_4() {
    __asm__ volatile("pop %rdx ; ret");
}

int gadget_5() {
    __asm__ volatile("pop %rax ; ret");
}

int main() {
    char buf[0x30];
    puts("GO GO GADGET POP A SHELL !! (: \n");
    fgets(buf, 0x400, stdin);
    return 0;
}
