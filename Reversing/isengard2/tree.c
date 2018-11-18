#include "tree.h"
#define HEIGHT(n) ((n == NULL) ? 0 : n->height)
#define MAX(a,b) ((a > b) ? a : b)
#define GET_BALANCE(n) ((n == NULL) ? 0 : HEIGHT(n->left) - HEIGHT(n->right))

node_t* right_rotate(node_t *y) 
{
    node_t *x = y->left;
    node_t *t2 = x->right;

    x->right = y;
    y->left = t2;

    y->height = (MAX(HEIGHT(y->left), HEIGHT(y->right))) + 1;
    x->height = (MAX(HEIGHT(x->left), HEIGHT(x->right))) + 1;

	return x;
}

node_t* left_rotate(node_t *x) 
{
    node_t *y = x->right;
    node_t *t2 = y->left;

    y->left = x;
    x->right = t2;

    x->height = (MAX(HEIGHT(x->left), HEIGHT(x->right))) + 1;
    y->height = (MAX(HEIGHT(y->left), HEIGHT(y->right))) + 1;

	return y;
}


node_t* insert(node_t* node, char val) 
{ 
    if (node == NULL) {
        node_t *result = (node_t*) malloc(sizeof(node_t));
        result->val = val;
        result->left = NULL;
        result->right = NULL;
        result->height = 1;
        return result;
    }
  
    if (val < node->val) 
        node->left  = insert(node->left, val); 
    else if (val > node->val) 
        node->right = insert(node->right, val); 
    else 
        return node; 
  
    node->height = 1 + MAX(HEIGHT(node->left), 
                           HEIGHT(node->right)); 
  
    int balance = GET_BALANCE(node); 
  
  
    if (balance > 1 && val < node->left->val) 
        return right_rotate(node); 
  
    if (balance < -1 && val > node->right->val) 
        return left_rotate(node); 
  
    if (balance > 1 && val > node->left->val) 
    { 
        node->left =  left_rotate(node->left); 
        return right_rotate(node); 
    } 
    if (balance < -1 && val < node->right->val) 
    { 
        node->right = right_rotate(node->right); 
        return left_rotate(node); 
    } 

    return node; 
} 

struct linked_node* end;
size_t node_count = 0;

struct linked_node {
    char val;
    struct linked_node* next;
};

void preorder(node_t *root) 
{
    if (root != NULL) {
        end->next = malloc(sizeof(struct linked_node));
        end = end->next;
        end->val = root->val;
        end->next = NULL;

        node_count++;

        preorder(root->left);
        preorder(root->right);
    }
}

bool test_flag(node_t *root)
{
    struct linked_node* start = malloc(sizeof(struct linked_node));
    start->next = NULL;

    end = start;
    preorder(root);
    struct linked_node* old = start;

    free(start);

    start = old->next;
    char* buf = malloc(sizeof(char) * (node_count));
    size_t k = 0;

    while (start != NULL) {
        old = start;

        buf[k++] = old->val ^ XOR_KEY;


        start = start->next;
        free(old);
    }

    bool result = strcmp(buf, TEST_KEY) == 0;
    free(buf);

    return result;
} 


