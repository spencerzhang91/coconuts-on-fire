/* C implementation of Linked List based graph ADT */
/* A more modern and reusable implementation */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "LinkedGraph.h"

static void MakeEdge(nodeptr header, nodeptr newnode);
static void traverselist(nodeptr header);

LGraph CreateGraph(int vn)
{
    /* initialize a gragh with vn vertexes but no edges */
    Vertex i;
    LGraph Graph = (LGraph)malloc(sizeof(struct Gnode));
    Graph->vertex_num = 7;
    Graph->edge_num = 0;
    for (i = 0; i < vn; i++)
    {
        Graph->G[i] = (nodeptr)malloc(sizeof(struct gnode));
        Graph->G[i]->adjv = i;
        Graph->G[i]->next = NULL;
    }
    return Graph;
}

void InsertEdge(LGraph graph, Edge e)
{
    /* for directed or undirected gragh to insert a new edge */
    nodeptr newnode = (nodeptr)malloc(sizeof(struct gnode));
    if (!newnode)
    {
        fprintf(stderr, "Memory is full, insert edge failed.\n");
        exit(EXIT_FAILURE);
    }
    newnode->adjv = e->vc;
    newnode->next = NULL;
    newnode->wt = e->wt;
    MakeEdge(graph->G[e->vr], newnode);
    // if graph is undirected:
    nodeptr mirror = (nodeptr)malloc(sizeof(struct gnode));
    mirror->adjv = e->vr;
    mirror->next = NULL;
    mirror->wt = e->wt;
    MakeEdge(graph->G[e->vc], mirror);
    graph->edge_num++;
}

void buildGraph(LGraph newgra)
{
    /* This function builds an directed graph adjacency lists by taking
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

void buildGraph_test(LGraph newgra)
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

void showmatrix(LGraph graph)
{
    int i;
    for (i = 0; i < graph->vertex_num; i++)
    {
        nodeptr curr = graph->G[i];
        while (curr)
        {
            printf("%d ", curr->adjv);
            curr = curr->next;
        }
        printf("\n");
    }
}

static void MakeEdge(nodeptr header, nodeptr newnode)
{
    if (!header)
    {
        fprintf(stderr, "arg1 of MakeEdge() if NULL.\n");
        exit(EXIT_FAILURE);
    }
    while (header->next)
        header = header->next;
    header->next = newnode;
}

static void traverselist(nodeptr header)
{
    while (header)
    {
        printf("%d ", header->adjv);
        header = header->next;
    }      
    printf("\n");
}
