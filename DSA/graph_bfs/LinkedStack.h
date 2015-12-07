/* C implementation of Linked List based Stack ADT */
/* A more modern and reusable implementation */
#ifndef _LINKEDSTACK_H
#include <stdbool.h>
#include "LinkedGraph.h"
#define _LINKEDSTACK_H
#define ElementType nodeptr  // can be changed according to particular purpose
#define MAX_STACK_SIZE 100

struct Node {
    ElementType data;
    struct Node *next;
};

typedef struct {
    struct Node *head;
    int maxsize;
    int cursize;
} Snode;

typedef Snode *Stack;

Stack CreateStack(int size);
bool IsFull(Stack S);
bool IsEmpty(Stack S);
void push(Stack S, ElementType item);
ElementType pop(Stack S);
ElementType top(Stack S);
void display(Stack S);

#endif
