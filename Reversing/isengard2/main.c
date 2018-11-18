#define _GNU_SOURCE
// TODO: 
// Fill in Checksum with actual checksum
// Timing check of program
// Check running processes for certain processes
// Hypervisor check on cpuinfo
// Add exception in breakpoint checker for the int3
// pack it
//
#define LOGO \
"        .__                                             .___       ________  \n" \
"        |__| ______ ____   ____    _________ _______  __| _/ ___  _\\_____  \\ \n" \
"        |  |/  ___// __ \\ /    \\  / ___\\__  \\\\_  __ \\/ __ |  \\  \\/ //  ____/ \n" \
"        |  |\\___ \\\\  ___/|   |  \\/ /_/  > __ \\|  | \\/ /_/ |   \\   //       \\ \n" \
"        |__/____  >\\___  >___|  /\\___  (____  /__|  \\____ |    \\_/ \\_______ \\\n" \
"                \\/     \\/     \\//_____/     \\/           \\/                \\/\n" \
"\n" \
"============================================================================================\n" \
"============================================================================================\n" \
"============================================================================================\n\n\n" \
"        \\\\\\\\\\                                                                  \\\\\\\\\\        \n" \
"          \\\\\\\\\\     Enter serial key:                                            \\\\\\\\\\      \n" \
"            \\\\\\\\\\                                                                  \\\\\\\\\\    \n\n\n" \
"============================================================================================\n" \
"============================================================================================\n" \
"============================================================================================\n\n\n" \

//#define DEBUGGED_TEST
volatile int CHECKSUM_VALUE = 0x4fed4843;

#include <dlfcn.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include <unistd.h>
#include <stdint.h>

#include <pthread.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/ptrace.h>
#include <sys/mman.h>
#include <ncurses.h>

#include "tree.h"

#define kms() \
    printf("no, bad"); \
    pid_t pid = getpid(); \
    kill(pid, SIGKILL);


#define dladdr_check(symbol, lib) {\
            void *dls_handle; \
            if (!(dls_handle = dlopen(lib, RTLD_LAZY)))  \
                exit(-1); \
            void *real_symbol = dlsym(dls_handle, symbol); \
            void *next_sym = dlsym(RTLD_NEXT, symbol); \
            if (real_symbol != next_sym) { \
                kms(); \
            } \
        }

#define SIGTRAP_ENTRY 0x401173
#define MOVSS asm("mov ax, ss;" \
             "mov ss, ax;"\
             "pushfw")


extern unsigned char* _start;
extern unsigned char* __etext;

void checksum()
{
    char* start =(char*) &_start;
    char* end = (char*) &__etext;

    unsigned checksum = 0;
    unsigned word = 0;

    unsigned counter = 0;

    while (start != end) {
        if (counter == 8) {
            checksum ^= word;
            word = 0;
            counter = 0;
        }
        word = (word << 8) | ((*(volatile unsigned*)start) & 0xFF);

        counter++;
        start++;
    }

    if (checksum != CHECKSUM_VALUE) {
        printf("hey wait you're not %x, you're %x!\n", CHECKSUM_VALUE, checksum);
        kms();
    }
}

void *antidebug_func(void *vargp) 
{
    dladdr_check("ptrace", "libc.so.6");

    uint8_t offset = 0;
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) == 0) {
        offset = 2;
    }
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {
        offset *= 3;
    }
    if (offset != 6) { 
        kms();
    }
}

void check_breakpoints() 
{
    char* start = (char*)&_start;
    char* end = (char*)&__etext;

    volatile unsigned char bppart[1] = { 0x66 };                  

    while(start != end) {
        if(((*(volatile unsigned*)start) & 0xFF) == ((*bppart) + (*bppart)) ) {

            printf("Naughtiness detected at %p: (%x)\n", start, *start);
            kms();
        }
        ++start;
    }
}

__attribute__((always_inline)) static inline void debugcheck(void)
{
    dladdr_check("kill", "libc.so.6");
    dladdr_check("pthread_create", "libpthread.so.0");

    pthread_t anti_debug_thread;
    pthread_create(&anti_debug_thread, NULL, antidebug_func, NULL);

    pthread_join(anti_debug_thread, NULL);
}

bool done_reading_crc = false;

struct crc_struct { char *input; }; 

void *check_crc(void *vargp) 
{
    MOVSS;
    struct crc_struct *s = (struct crc_struct *) vargp;

    while (!done_reading_crc)
        ;

    sleep(3);
    node_t *tree = NULL;

    for (int i = 0; s->input[i] != '\x00'; i++) {
        tree = insert(tree, s->input[i]);
    }

    if (test_flag(tree)) {
        printf("Correct!");
    } else {
        printf("Wrong!");
    }
}

__attribute__((section("UPX1")))void main_handler(int signo) 
{
    MOVSS;
    int delay = 1;

    char *input = malloc(sizeof(char) * 31);

    pthread_t crc_checker_thread;
    struct crc_struct *args = malloc(sizeof(struct crc_struct));
    args->input = input;

    pthread_create(&crc_checker_thread, NULL, check_crc, (void *)args);
    initscr();
    noecho();

	printw(LOGO);
    while (!done_reading_crc) {
        int ch = 0;

        size_t len = 0;

        move(13, 38);
        while (ch != 0xa && len < 30) {
            ch = getch();
            printw("%c", ch);
            input[len] = ch;

            len++;
        }
        if (len <= 0) {
            kms();
        }

        input[len - 1] = '\0';
        clear();
        refresh();
        done_reading_crc = true;
    }
    pthread_join(crc_checker_thread, NULL);
    endwin();
    free(input);

    return;
}


int main(int argc, char* argv[])
{
    MOVSS;

#ifndef DEBUGGED
    debugcheck();
#endif

    checksum();

    signal(SIGTRAP, main_handler);
    main_handler(3); 

    return 0;
}
