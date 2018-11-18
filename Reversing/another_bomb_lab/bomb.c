#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#define MAX_CHARS 10000

// safe_usub -- perform safe unsigned subtraction
size_t safe_usub (size_t x, size_t y) {
    return x > y ? x - y : y - x ;
}

void get_flag() {
    char flag[28];
    FILE* file;
    file = fopen("flag.txt", "r");
    fgets(flag, 28, file);
    printf("%s\n", flag);
}

void explode() {
    printf("Oh no...\n");
    sleep(1);
    char* boom = "     _.-^^---....,,--       \n _--                  --_  \n<                        >)\n|                         | \n \\._                   _./  \n    ```--. . , ; .--'''      \n          | |   |             \n       .-=||  | |=-.   \n       `-=#$%&%$#=-'  \n          | ;  :|    \n _____.,-#%&$@%#&#~.,_____";
    printf("%s\n", boom);
    exit(0);
}

int if_valid(int number) {
    if (number <= 1) {
        return 0;
    } else if (number < 4) {
        return 1;
    } else if (number % 2 == 0 || number % 3 == 0) {
        return 0;
    }
    int i = 5;
    while (i * i < number) {
        if (number % i == 0 || number % (i + 2) == 0) {
            return 0;
        }
        i = i + 2;
    }
    return 1;
}

int number_n(int number) {
    int i;
    int count = 1;
    for (i = 3; ; i += 2) {
        if (if_valid(i)) {
            count++;
            if (count == number) {
                return i;
            }
        }
    }
}

void phase_three() {
    int val = number_n(343);
    int user_val;
    scanf("%d", &user_val);
    if (user_val == val) {
        get_flag();
    } else {
        explode();
    }
}

void manipulate(int* array) {
    int i, j;
    int holder;
    for (i = 0; i < 8; i++) {
        for (j = i + 1; j < 8; j++) {
            if (array[i] < array[j]) {
                holder = array[i];
                array[i] = array[j];
                array[j] = holder;
            }
        }
    }
}

void phase_two() {
    int arr[8] = {15, 67, 44, 38, 21, 99, 163, 23};
    manipulate(arr);
    int i;
    int user_arr[8];
    for (i = 0; i < 8; i++) {
        scanf("%d", &user_arr[i]);
    }
    for (i = 0; i < 8; i++) {
        if (user_arr[i] != arr[i]) {
            explode();
        }
    }
    printf("Oh heeey cool got that one too.\n Final Round!\n");
}

char* strrev (char*  str) {
    if (!str) { return NULL; }
    size_t len = strnlen(str, MAX_CHARS);
    char*  new = malloc( sizeof(char) * len );
    size_t i;
    for (i = 0; i < len; i++) {
        new[i] = str[safe_usub(i + 1, len)];
    }
    new[i] = 0;
    return new;
}

void phase_one(char* choice, char* orig) {
    char* good_pass = strrev(orig);
    char* new_line;
    new_line = strchr(choice, '\n');
    *new_line = '\0';
    if (strcmp(choice, good_pass) == 0) {
        printf("Cool you got that one, time for round two.\n");
        //get_flag();
    } else {
        explode();
    }
}

int main(){
    char* pass_phrase = "no_booms_today";
    char user_word[256];
    printf("Here is a bomb, defuse it and save yourself.\nEnter the secret pass phrase.\n");
    fgets(user_word, sizeof(user_word), stdin);
    phase_one(user_word, pass_phrase);
    phase_two();
    phase_three();
    return 0;
}
