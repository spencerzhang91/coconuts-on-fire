/* C implementation of Linked List based graph ADT */
/* A more modern and reusable implementation */
#ifndef _LINKEDGRAPH_H
#define _LINKEDGRAPH_H
#define MaxVertexNum 100
typedef int Vertex;                         // subfix to represent vertex
typedef int Weight;                         // use int to represent weight
typedef char DataType;                      // data type of vertex data

/* definition of edge */
typedef struct edge *Edge;
struct edge {
    Vertex vr;                              // row subfix
    Vertex vc;                              // col subfix
    Weight wt;                               // weight of the edge
};

/* definition of adjacency node */
typedef struct node *nodeptr;
struct node {
    Vertex adjv;
    Weight wt;
    DataType data;
    nodeptr next;
};

/* definition of linked lists based graph */
typedef struct Gnode *LGraph;
struct Gnode {
    int vertex_num;
    int edge_num;
    nodeptr G[MaxVertexNum];                    // adjacency linked list
};

LGraph CreateGraph(int vn);
void InsertEdge(LGraph gragh, Edge e);
void buildGraph(LGraph newgra);
void buildGraph_test(LGraph newgra);
void showmatrix(LGraph graph);

#endif 