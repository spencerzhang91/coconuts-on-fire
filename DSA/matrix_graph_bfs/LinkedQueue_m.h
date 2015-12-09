/* Linked list based Queue ADT implementation */
/* header files */
#ifndef _LINKEDQUEUE_H
#define _LINKEDQUEUE_H
#include "MatrixGraph.h"
#define ElementType int // can be changed according to particular purpose
#define MAXSIZE 100

typedef struct qnode *Node;
struct qnode {
    ElementType data;
    Node next;
};

typedef struct Qnode *Queue;
struct Qnode {
    Node front;
    Node rear;
    int cursize;
    int maxsize;
};

Queue CreateQueue(int maxsize);
bool QIsFull(Queue Q);
bool QIsEmpty(Queue Q);
void enqueue(Queue Q, ElementType item);
ElementType dequeue(Queue Q);

#endif
