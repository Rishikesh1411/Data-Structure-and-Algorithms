"""  
     ASSIGNMENT-22 (ADJACENCY MATRIX IMPLEMENTATION OF GRAPH)

     1.WRITE A CLASS GRAPH TO IMPLEMENT ADJACENCY MATRIX REPRESENTATION OF A SIMPLE AND UNDIRECTED GRAPH

     2.IN CLASS GRAPH .DEFINE __INIT__() METHOD TO INITIALIZE VERTEX_COUNT AND ADJ_MATRIX(LISTS OF LISTS)

     3.IN CLASS GRAPH,DEFINE ADD_EDGE() METHOD ADD AN EDGE IN THE GRAPH WITH GIVEN WEIGHT

     4.IN CLASS GRAPH DEFINE REMOVE _EDGE() METHOD TO REMOVE AN EDGE FROM THE GRAPH

     5.IN CLASS GRAPH DEFINE HAS_EDGE() METHOD TO CHECK WETHER TWO GIVEN VERTICES ARE CONNECTED BY AN EDGE OR NOT

     6.IN CLASS GRAPH, DEFINE PRINT_ADJ_MATRIX() METHOD TO PRINT ADJACENCY MATRIX


"""


class Graph:
    def __init__(self,vertex_count):
        self.vertex_count = vertex_count
        self.adj_matrix = [[0]*vertex_count for i in range(vertex_count)] ##no of vwertex count time this matrix will repeat
    

    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and  0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight ##since graph is undirected so edge will be present
        else:
            print("invalid vertex")

    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and  0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("invalid vertex")

    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and  0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("invalid vertex")

        
    def  print_adj_matrix(self):
        for row in self.adj_matrix:
             print(" ".join(map(str,row)))


g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.print_adj_matrix()

        

