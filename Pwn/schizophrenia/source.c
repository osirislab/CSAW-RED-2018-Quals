#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned long long uint64_t;

typedef struct {
  void (*do_the_thing)()
} thing;

void* things[11];
int is_thing[11];

uint64_t get_index() {
  char buf[255];
  fgets(buf, 255, stdin);

  uint64_t index = strtoull(buf, NULL, 10);

  if (index > 10) {
    printf("I'm being dragged awayyyyyyyy\n");
    exit(1);
  }

  return index;
}

void make_string(uint64_t index) {
  printf("How loud do you need your voice to be?\n");

  char buf[255];
  fgets(buf, 255, stdin);
  uint64_t length = strtoull(buf, NULL, 10);

  if (length > 1024) {
    printf("Too loud!\n");
    return;
  }

  char* voice = malloc(length);

  printf("What should your voice say?\n");
  uint64_t nbytes = read(0, voice, length);
  voice[nbytes] = 0; // This is the single-byte overflow

  things[index] = voice;
  is_thing[index] = 0;
}

void make_thing(uint64_t index) {
  printf(
    "Ok making things!\n"
    "Keeping yourself occupied is always a great way to distract from the voices\n"
  );

  thing* t = malloc(sizeof(thing));

  things[index] = t;
  is_thing[index] = 1;
}

void alloc() {
  printf("Which one?\n");

  uint64_t index = get_index();

  if (things[index] != NULL) {
    printf("There is another voice here already!\n");
    return;
  }

  printf("Which type? (voice/thing)\n");

  char buf[255];
  fgets(buf, 255, stdin);

  if (strcmp(buf, "voice\n") == 0) {
    make_string(index);
  } else if (strcmp(buf, "thing\n") == 0) {
    make_thing(index);
  } else {
    printf("That is not a valid answer\n");
  }
}

void kill() {
  printf("Which one?\n");

  uint64_t index = get_index();

  printf("QUIET YOU!\n");
  free(things[index]);
  things[index] = NULL;
}

void fidget() {
  printf("Which one?\n");

  uint64_t index = get_index();

  if (!is_thing[index]) {
    printf("I can't do anything with a voice swirling around up here!\n");
    return;
  }

  ((thing*)things[index])->do_the_thing();
}

void print_flag() {
  FILE* f = fopen("flag.txt", "r");
  char buf[255];
  fgets(buf, 255, f);

  printf("%s\n", buf);
}

int main() {

  while(1) {
    printf("The voices!\n");
    uint64_t choice = get_index();

    switch(choice) {
    case 1:
      alloc();
      break;
    case 2:
      kill();
      break;
    case 3:
      fidget();
      break;
    default:
      break;
    }
  }
}