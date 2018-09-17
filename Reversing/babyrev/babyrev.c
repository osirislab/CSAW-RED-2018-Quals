#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int64_t get_number(){
    char buf[0x80];
    fgets(buf, sizeof(buf), stdin);
    return strtol(buf, NULL, 10);
}

void win(){
    char buf[0x80];
    FILE *file;
    if ((file = fopen("flag.txt", "r")) != NULL) {
        fgets(buf, sizeof(buf), file);
        printf("Here's your flag, friend: %s\n", buf);
    } else {
        puts("ERROR: no flag found. If you're getting this error on the remote "
             "system, please message the admins. If you're seeing this locally, "
             "run it on the remote system! You solved the challenge, and need to "
             "get the flag from there!");
    }
}

void lose(){
    printf("Not Quite ): KEEEEEP TRYYYIINNG !!!\n");
    exit(100);
}

bool check(int64_t special, int64_t num){
    return (((num ^ (special % 100)) * 3) - 1) == 0x1337;
}

int main(int argc, char ** argv){
    printf("\n\nWelcome to BabyRev can you crack the code???\n\n");
    for (size_t i = 0; i < 100; ++i){
        int64_t special = rand();
		int64_t num = get_number();
		
		if (!(check(special, num))){
			lose();
 		}
        printf("YAAAY Keep GOING !!\n");
    }
	win();
    return 0;
}
