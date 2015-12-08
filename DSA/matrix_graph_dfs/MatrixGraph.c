/* C implementation of Matrix based graph ADT */
/* A more modern and reusable implementation */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "MatrixGraph.h"

MGraph CreateGraph(int vn)                  // vn for vertex number
{
    /* initialize a graph with vn vertexes but no edges */
    Vertex i, j;
    MGraph Graph = (MGraph)malloc(sizeof(struct graph));
    Graph->vertex_num = vn;
    Graph->edge_num = 0;
    /* initialize the adjacency matrix */
    for (i = 0; i < vn; i++)
        for (j = 0; j < vn; j++)
            Graph->G[i][j] = INFINITY; // initialization weight
    return Graph;
}

void InsertEdge(MGraph g, Edge e)
{
    g->G[e->vr][e->vc] = e->wt;
    // if graph is undirected add the following one line:
    g->G[e->vc][e->vr] = e->wt; 
    g->edge_num++;
}

void buildGraph(MGraph newgra)
{
    /* This function builds an directed graph adjacency matrix by taking
     pairs of connections */
    int row, col, weight;
    printf("Please input a pair of connected nodes(vr-vc:w)"
        " to the %d nodes graph:\n", newgra->vertex_num);
    while (scanf("%d-%d:%d", &row, &col, &weight) == 3)
    {
        Edge newedge = (Edge)malloc(sizeof(struct edge));
        newedge->vr = row; newedge->vc = col; newedge->wt = weight;
        InsertEdge(newgra, newedge);
        printf("New edge inserted to the graph.\n");
    }
}

void buildGraph_test(MGraph newgra)
{
    /* test version of buildGraph, the original graph is on page180 */
    int row[8] = {0,0,1,1,2,3,3,4};
    int col[8] = {1,5,2,6,3,4,6,5};
    for (int i = 0; i < 8; i++)
    {
        Edge newedge = (Edge)malloc(sizeof(struct edge));
        newedge->vr = row[i];
        newedge->vc = col[i];
        newedge->wt = 1;
        InsertEdge(newgra, newedge);
    }
    printf("Test graph created.\n");
}

void showmatrix(MGraph graph)
{
    int i, j;
    int max = graph->vertex_num;
    for (i = 0; i < max; i++)
    {
        for (j = 0; j <max; j++)
        {
            if (graph->G[i][j] != INFINITY)
                printf("%d ", graph->G[i][j]);
            else
                printf("0 ");
        }
        puts("");
    }
}
