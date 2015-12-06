/* The iterative implementation of depth first search of graph */
#include <stdio.h>
#include <stdlib.h>
#include "LinkedStack.h"
#include "LinkedGraph.h"

/* Modified definition of dfs: support function pointer as an argument */
void dfs_iterative(LGraph graph, Vertex start, void (*func)(nodeptr p));
nodeptr nextunvisited(nodeptr curr, int visited[]);
void visit(nodeptr p);

int main(void)
{
    int vertices = 10;
    LGraph tg = CreateGraph(vertices);
    buildGraph_test(tg);
    showmatrix(tg);
    dfs_iterative(tg, 0, visit);

    return 0;
}

void dfs_iterative(LGraph graph, Vertex start, void (*func)(nodeptr p))
{
    int visited[graph->vertex_num]; // rest elements init automaticly
    Stack stack = CreateStack(MAX_STACK_SIZE);
    nodeptr curr, startnode;
    curr = startnode = graph->G[start];
    
    (*func)(curr);
    push(stack, curr);
    visited[curr->adjv] = 1;
    
    while (curr->adjv != start || stack)
    {
        nodeptr temp = nextunvisited(curr, visited);
        if (temp)
            curr = graph->G[temp->adjv];
        else curr = NULL;
        if (curr)
        {
            (*func)(curr);
            visited[curr->adjv] = 1;
            push(stack, curr);
        }
        else curr = pop(stack);
    }
}

nodeptr nextunvisited(nodeptr curr, int visited[])
{
    // printf("curr is: \n", curr->adjv);
    curr = curr->next;
    while (curr)
    {
        if (visited[curr->adjv] == 1)
            curr = curr->next;
        else return curr;
    }
    return NULL;
}

void visit(nodeptr p)
{
    printf("visiting vertext %d\n", p->adjv);
}
