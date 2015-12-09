/* Linked list based Queue ADT implementation */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "LinkedQueue_m.h"

Queue CreateQueue(int maxsize)
{
    Queue temp = (Queue)malloc(sizeof(struct Qnode));
    temp->front = temp->rear = NULL;
    temp->maxsize = maxsize;
    temp->cursize = 0;
    return temp;
}

bool QIsFull(Queue Q)
{
    return Q->cursize == Q->maxsize;
}

bool QIsEmpty(Queue Q)
{
    return Q->front == NULL;
}

void enqueue(Queue Q, ElementType item)
{
    Node rearcell;
    ElementType rearelem = item;
    if (QIsFull(Q))
    {
        printf("The queue is Full.\n");
        exit(1);
    }   
    else
    {
        rearcell = (Node)malloc(sizeof(struct qnode));
        rearcell->data = rearelem;
        if (Q->cursize == 0)
            Q->front = Q->rear = rearcell;
        else
        {
            Q->rear->next = rearcell;
            Q->rear = Q->rear->next;
        }    
        ++Q->cursize;
    }
}

ElementType dequeue(Queue Q)
{
    Node frontcell;
    ElementType frontelem;
    if (QIsEmpty(Q))
    {
        printf("The queue is empty.\n");
        return NULL; 
    }
    else
    {
        frontcell = Q->front;
        frontelem = frontcell->data;
        if (Q->front == Q->rear)
            Q->front = Q->rear = NULL;
        else
            Q->front = Q->front->next;
        free(frontcell);
        --Q->cursize;
        return frontelem;
    }
}
