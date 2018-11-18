#pragma once
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// based off of https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

#define XOR_KEY 69
#define TEST_KEY "\x28\x20\x05\x65\x26\x24\x2e\x2c\x29\x35\x2b\x2a\x30\x36\x37\x31\x3c"

typedef struct node 
{
    struct node *left;
    struct node *right;
    int height;

    char val;
} node_t;

node_t* right_rotate(node_t *y);
node_t* left_rotate(node_t *y);
node_t* insert(node_t *root, char val);

bool test_flag(node_t *tree);
