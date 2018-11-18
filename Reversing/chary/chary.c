#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int check_char_0(char chr) {
    register uint8_t ch = (uint8_t) chr;
    ch ^= 97;

    if(ch != 2) {
        exit(1);
    }
    return 1;
}

int check_char_1(char chr) {
    register uint8_t ch = (uint8_t) chr;
    ch ^= 112;
    ch += 112;
	ch &= 1;
	ch += 114;

    if(ch != 115) {
        exit(1);
    }
    return 1;
}

int check_char_2(char chr) {
    register uint8_t ch = (uint8_t) chr;
    ch += 61;
    ch -= 76;

    if(ch != 82) {
        exit(1);
    }
    return 1;
}

int check_char_3(char chr) {
    register uint8_t ch = (uint8_t) chr;
    ch ^= 149;

    if(ch != 226) {
        exit(1);
    }
    return 1;
}

int check_char_4(char chr) {
    register uint8_t ch = (uint8_t) chr;
    ch ^= 19;
    ch *= 2;

    if(ch != 130) {
        exit(1);
    }
    return 1;
}

int check_char_5(char chr) {
    register uint8_t ch = (uint8_t) chr;
    ch ^= 5;
    ch *= 3;
    ch -= 100;

    if(ch != 188) {
        exit(1);
    }
    return 1;
}

int check_char_6(char chr) {
    register uint8_t ch = (uint8_t) chr;
    ch += 71;

    if(ch != 171) {
        exit(1);
    }
    return 1;
}

int check_char_7(char chr) {
    register uint8_t ch = (uint8_t) chr;
    ch ^= 41;

    if(ch != 111) {
        exit(1);
    }
    return 1;
}

int check_char_8(char chr) {
    register uint8_t ch = (uint8_t) chr;
    ch += 41;
    ch += 53;

    if(ch != 210) {
        exit(1);
    }
    return 1;
}

int check_char_9(char chr) {
    register uint8_t ch = (uint8_t) chr;
    ch ^= 61;
    ch += 41;
    ch += 11;

    if(ch != 126) {
        exit(1);
    }
    return 1;
}

int check_char_10(char chr) {
    register uint8_t ch = (uint8_t) chr;
    ch ^= 47;
    ch += 29;
    ch += 67;

    if(ch != 110) {
        exit(1);
    }
    return 1;
}


int check(char *buf) {
    check_char_0(buf[0]);
    check_char_1(buf[1]);
    check_char_2(buf[2]);
    check_char_3(buf[3]);
    check_char_4(buf[4]);
    check_char_5(buf[5]);
    check_char_6(buf[6]);
    check_char_7(buf[7]);
    check_char_8(buf[8]);
    check_char_9(buf[9]);
    check_char_10(buf[10]);

    return 1;
}

void give_flag() {
    FILE *flag = fopen("flag.txt", "r");
    if (!flag) {
        puts("flag.txt not found. If you were running this against the remote server, you'd have the flag right now. If you are seeing this when connected to the server, something has gone horribly wrong, and you should contact the admins!");
        return;
    }

    char buf[128];
    fgets(buf, sizeof(buf)-1, flag);
    puts(buf);
}


int main() {
    char buf[12];
    puts("Enter secret message: \n");
    fgets(buf, 12, stdin);
    check(buf);
    give_flag();
    return 0;
}
