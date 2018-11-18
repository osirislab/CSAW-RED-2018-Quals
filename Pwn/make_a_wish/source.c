#include <stdio.h>
#include <stdlib.h>

void shellebration(){
	system("/bin/sh");
}

int main(int argc, char** argv)
{
    printf("Hello, it's my birthday.\n");
    printf("Say something nice to me and we gonna shellebrate: \n");
    int yayyy;
    char buffer[100];
    yayyy = 0;
    gets(buffer); 
    if (yayyy == 21)
    {
        shellebration();
    }
    else if (yayyy != 21 && yayyy != 0){
        printf("I am turning 21!");
    }
    else
    {
        printf("You need to be more extra :)\n");
    }
    return 0;
}
