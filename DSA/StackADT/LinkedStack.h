/* C implementation of Linked List based Stack ADT */
/* A more modern and reusable implementation */
#ifndef _LINKEDSTACK_H
#include <stdbool.h>
#define _LINKEDSTACK_H
#define ElementType int
#define MAX_STACK_SIZE 100

struct Node {
    ElementType data;
    struct Node *next;
};

typedef struct Snode *Stack;
struct Snode{
    struct Node *head;
    int maxsize;
    int cursize;
};

Stack CreateStack(int size);
bool IsFull(Stack S);
bool IsEmpty(Stack S);
void push(Stack S, ElementType item);
ElementType pop(Stack S);
ElementType top(Stack S);
void display(Stack S);

#endif