/* The iterative implementation of depth first search of graph */
/* Graph ADT based on adjacency matrix storage */
#include <stdio.h>
#include <stdlib.h>
#include "LinkedStack_m.h"
#include "MatrixGraph.h"

/* Modified definition of dfs: support function pointer as an argument */
void dfs_iterative(MGraph graph, Vertex start, void (*func)(int p));
int nextunvisited(int curr, int visited[]);
void visit(int p);

int main(void)
{
    int vertices = 7;
    MGraph tg = CreateGraph(vertices);
    buildGraph_test(tg);
    showmatrix(tg);
    dfs_iterative(tg, 0, visit);

    return 0;
}
// p is the vertex number of the 
void dfs_iterative(MGraph graph, Vertex start, void (*func)(int p))
{
    int visited[graph->vertex_num];
    Stack stack = CreateStack(MAX_STACK_SIZE);
    int curr;
    curr = start; // here curr marks current vertex
    
    (*func)(curr);
    push(stack, curr);
    visited[curr] = 1;
    
    while (curr != start || !IsEmpty(stack))
    {
        int flag = 0;
        for (int i = 0; i < graph->vertex_num; i++)
            if ((graph->G[curr][i] == 1) && (visited[i] != 1))
            {
                curr = i;
                flag++;
                break;
            }
        if (flag)
        {
            (*func)(curr);
            visited[curr] = 1;
            push(stack, curr);
            display(stack); // check point
        }    
        else
            curr = pop(stack);
    }
}

void visit(int p)
{
    printf("visiting vertext %d\n", p);
}
