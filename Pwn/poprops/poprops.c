#include <stdio.h>
#include <stdlib.h>

char * itsame = "/bin/sh\x00";

void run_cmd(char * cmd){
    system(cmd);
}

int gadget(){
    __asm__ volatile("pop %rdi ; ret");
}

int main(int argc, char ** argv){
    char buf[37];
    puts("Welcome to poprop!; Are you're skills of the chain??");
    gets(buf);
    return 0;
}
