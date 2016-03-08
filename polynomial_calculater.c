// Problem 1: polynomial calculator
// definition of polynomial storage structure (using a linked list)
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct PolyNode *Polynomial;
struct PolyNode {
    int coef;
    int expo;
    Polynomial next;
};
// method definition:
Polynomial readpoly(void);  // read polynomial in
void attach(int c, int e, Polynomial *pRear); // helper func of readpoly
void display(Polynomial p); // print out the polynomial
Polynomial multiply(Polynomial p1, Polynomial p2);
Polynomial sumpoly(Polynomial p1, Polynomial p2);
int Compare(int a, int b);

int main(void)
{
    Polynomial p1, p2, multiply_p, sum_p;

    p1 = readpoly();
    p2 = readpoly();
    multiply_p = multiply(p1, p2);
    sum_p = sumpoly(p1, p2);

    display(multiply_p);
    display(sum_p);

    return 0;
}

Polynomial readpoly(void)
{
    Polynomial P, rear, temp; // temp is temporary node
    int c, e, N;
    scanf("%d", &N);
    P = (Polynomial)malloc(sizeof(struct PolyNode));
    P->next = NULL;
    rear = P;
    while (N--)
    {
        scanf("%d %d", &c, &e);
        attach(c, e, &rear);  // add current node to the end of polynomial
    }
    temp = P;
    P = P->next;
    free(temp);
    return P;
}

void attach(int c, int e, Polynomial *pRear)
{
    // pRear point to the last node of the linked list
    Polynomial P;
    P = (Polynomial)malloc(sizeof(struct PolyNode));
    P->coef = c;
    P->expo = e;
    P->next = NULL;
    (*pRear)->next = P;
    *pRear = P;
}

Polynomial sumpoly(Polynomial p1, Polynomial p2)
{
    Polynomial front, rear, temp;
    int sum;
    rear = (Polynomial)malloc(sizeof(struct PolyNode));
    front = rear; // front keeps the head node of result nexted list
    while (p1 && p2)
    {
        switch (Compare(p1->expo, p2->expo))
        {
            case 1:
                attach(p1->coef, p1->expo, &rear);
                p1 = p1->next;
                break;
            case -1:
                attach(p2->coef, p2->expo, &rear);
                p2 = p2->next;
                break;
            case 0:
                sum = p1->coef + p2->coef;
                if (sum)
                    attach(sum, p1->expo, &rear);
                p1 = p1->next;
                p2 = p2->next;
                break;
        }
    }
    while (p1)
    {
        attach(p1->coef, p1->expo, &rear);
        p1 = p1->next;
    }
    while (p2)
    {
        attach(p2->coef, p2->expo, &rear);
        p2 = p2->next;
    }
    rear->next = NULL;
    temp = front;
    front = front->next;
    free(temp);
    return front;
}

Polynomial multiply(Polynomial p1, Polynomial p2)
{
    Polynomial p, rear, t1, t2, t;
    int c, e;
    if (!p1 || !p2)
        return NULL;
    t1 = p1;
    t2 = p2; // temp holder
    p = (Polynomial)malloc(sizeof(struct PolyNode));
    p->next = NULL;
    rear = p;
    while (t2)
    {
        attach(t1->coef * t2->coef, t1->expo + t2->expo, &rear);
        t2 = t2->next;
    }
    t1 = t1->next;
    while (t1)
    {
        t2 = p2;
        rear = p;
        while (t2)
        {
            e = t1->expo + t2->expo;
            c = t1->coef * t2->coef;
            while (rear->next && rear->next->expo > e)
                rear = rear->next;
            if (rear->next && rear->next->expo == e)
            {
                if (rear->next->coef + c)
                    rear->next->coef += c;
                else
                {
                    t = rear->next;
                    rear->next = t->next;
                    free(t);
                }
            }
            else
            {
                t = (Polynomial)malloc(sizeof(struct PolyNode));
                t->coef =c;
                t->expo = e;
                t->next = rear->next;
                rear->next = t;
                rear = rear->next;
            }
        }
    }
    t2 = p;
    p = p->next;
    free(t2);

    return p;
}

void display(Polynomial p)
{
    int flag = 0; // for better formatting
    if (!p)
    {
        printf("0 0\n");
        return;
    }
    while (p)
    {
        if (!flag)
            flag = 1;
        else
            printf(" ");
        printf("%d %d", p->coef, p->expo);
        p = p->next;
    }
    printf("\n");
}

int Compare(int a, int b)
{
    if (a > b)
        return 1;
    else if (a < b)
        return -1;
    else
        return 0;
}