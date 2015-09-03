/* a simple binary tree */
/* simpletree.h */
#ifndef _TREE_
#define _TREE_

typedef struct node {
    int num;
    struct node *left;
    struct node *right;
} Node;

typedef struct tree {
    Node *root;
    int size = 0;
};

void AddNode(const Node *new_node, Node *root);
void DeleteNode(int val, Node *root);
#endif


