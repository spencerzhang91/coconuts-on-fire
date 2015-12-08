/* C implementation of Linked List based Stack ADT */
/* A more modern and reusable implementation, for MatrixGraph use only */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "LinkedStack_m.h"

Stack CreateStack(int size)
{
    Stack newS = (Stack)calloc(size, sizeof(Snode));
    newS->head = (struct Node *)calloc(size, sizeof(struct Node));
    newS->head->next = NULL;
    newS->cursize = 0;
    newS->maxsize = size;
    return newS;
}

bool IsFull(Stack S)
{
    return S->cursize == S->maxsize;
}

bool IsEmpty(Stack S)
{
    return S->cursize == 0;
}

void push(Stack S, ElementType item)
{
    if (IsFull(S))
    {
        fprintf(stderr, "The stack is full.\n");
        exit(EXIT_FAILURE);
    }
    else
    {
        struct Node *temp = (struct Node *)malloc(sizeof(struct Node));
        temp->data = item;
        temp->next = S->head;
        S->head = temp;
        S->cursize++;
    }
}

ElementType pop(Stack S)
{
    if (IsEmpty(S))
    {
        fprintf(stderr, "The stack is empty.\n");
        exit(EXIT_FAILURE);
    }
    else
    {
        ElementType res = S->head->data;
        S->head = S->head->next;
        S->cursize--;
        return res;
    }
}

ElementType top(Stack S)
{
    return S->head->data;
}

void display(Stack S)
{
    Stack temp = (Stack)malloc(sizeof(Stack));
    temp->head = (struct Node *)malloc(sizeof(struct Node));
    temp->head = S->head;
    while (temp->head->next != NULL)
    {
        printf("%d ", temp->head->data);
        temp->head = temp->head->next;
    }
    putchar('\n');
}
