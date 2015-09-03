/* implementation of simple tree */
/* simpletree.c */
#include "simpletree.h"

void AddNode(const Node *new_node, Node *root)
{
    if (root == NULL)
        root = new_node;
        
    if (new_node->num < root->num)
    {
        if (root->left == NULL)
            root->left = new_node;
        else
            AddNode(new_node, root->left)
    }
        
    else if (new_node->num > root->num)
    {
        if (root->right == NULL)
            root->right = new_node;
        else
            AddNode(new_node, root->right)
    }
    else
        puts("Attemping to add duplicate node");
}

void DeleteNode(int val, Node *root)
{
    
}
