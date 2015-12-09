/* C implementation of adjacency matrix based graph ADT */
/* A more modern and reusable implementation */
#ifndef _MATRIXGRAPH_H
#define _MATRIXGRAPH_H
#define MaxVertexNum 100
#define INFINITY 65535
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
/* definition of graph */
typedef struct graph *MGraph;
struct graph {
    int vertex_num;
    int edge_num;
    Weight G[MaxVertexNum][MaxVertexNum];   // the adjacency matix
    DataType Data[MaxVertexNum];            // data saved on vertexes
};

MGraph CreateGraph(int vn);
void InsertEdge(MGraph g, Edge e);
void buildGraph(MGraph newgra);
void buildGraph_test(MGraph newgra);
void showmatrix(MGraph graph);

#endif