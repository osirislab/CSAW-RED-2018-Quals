#include "tree.h"

void pre_order(node_t *root) 
{
	if (root != NULL) {
        printf("%d ", root->val);
        pre_order(root->left);
        pre_order(root->right);
	}
}

int main() {
    node_t* root = NULL;
    char* random_key = "pm @tnek your complaints";

    for (int i = 0; random_key[i] != '\x00'; i++) {
        root = insert(root, random_key[i]);
    }

    printf("Flag gen: ");
    pre_order(root);
    printf("\n");


    node_t *tree = NULL;

    for (int i = 0; random_key[i] != '\x00'; i++) {
        tree = insert(tree, random_key[i]);
    }

    printf("%d ", test_flag(tree));
}
 
