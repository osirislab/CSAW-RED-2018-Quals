#include <stdio.h>
#include <stdlib.h>

void give_shell(){
    system("/bin/sh");
}

int main(int argc, char ** argv){
    char buf[69];
    puts("What is your favorite thing ? \n");
    gets(buf);

    printf("I like, %s too!!! \n", buf);
    return 0;
}
