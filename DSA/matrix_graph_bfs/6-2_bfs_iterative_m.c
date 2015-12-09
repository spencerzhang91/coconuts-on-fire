/* The recursive implementation of depth first search of graph */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "MatrixGraph.h"  // organized graph ADT
#include "LinkedQueue_m.h"  // organized queue ADT

/* Modified definition of bfs: support function pointer as an argument */
void bfs_iterative(MGraph graph, Vertex start, void (*func)(int p));
void visit(int p);

int main(void)
{
    int vertices = 7;
    MGraph tg = CreateGraph(vertices);
    buildGraph_test(tg);
    showmatrix(tg);
    bfs_iterative(tg, 0, visit);
    
    return 0;
}

void bfs_iterative(MGraph graph, Vertex start, void (*func)(int p))
{
    int visited[graph->vertex_num];
    Queue queue = CreateQueue(graph->vertex_num);
    int curr;
    curr = start; // 
    visited[curr] = 1;
    enqueue(queue, curr);
    
    while (!QIsEmpty(queue))
    {        
        for (int i = 0; i < graph->vertex_num; i++)
            if ((graph->G[curr][i] == 1) && (visited[i] != 1))
            {
                enqueue(queue, i);
                visited[i];
            }
        curr = dequeue(queue);
        (*func)(curr);
    }
}

void visit(int p)
{
    printf("visiting vertext %d\n", p);
}
