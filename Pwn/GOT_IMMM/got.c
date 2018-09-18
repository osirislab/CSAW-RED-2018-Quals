#include <stdio.h>
#include <string.h>
#include <unistd.h>

char buf[24];

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
}

void run_cmd(char *cmd) {
    system(cmd);
}

int main() {
    struct {
        char val[24];
        char *addr;
    } a;

    a.addr = buf;

    init();

    printf("Welcome! The time is ");
    run_cmd("/bin/date");
    printf("Anyways, give me a string to save: ");
    fgets(a.val, sizeof(a), stdin);
    printf("Ok, I'm writing %s to my buffer...\n", a.val);
    memcpy(a.addr, a.val, sizeof(a.val));
    puts(a.val);
    return 0;
}
