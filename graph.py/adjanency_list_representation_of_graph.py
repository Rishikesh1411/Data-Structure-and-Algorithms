"""

   Assignment-23

   1.write a class graph to implement list representation of a graph data structure

   2.in class graph .define __init__() method to initialise object veriables vertex_count and a dict
    adj_list  where key is vertex number and value is a list of adjacent vertices

   3.in class graph define add_edge() method to add an edge in the graph with given vertices and weight

   4.in class graph defien remove edge() method to remove an edge from the graph

   5.in classs graph define has_edge() method to check whether an edge exists or not for a given pair of vertices.

   6.in class graph ,define print_adj__list() method to print adjanancy lists of graph.


"""

class Graph:
    def __init__(self,vertex_count):
        self.vertex_count=vertex_count
        self.adj_list={k:[] for k in range(vertex_count)}

    
    def  add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print("Invalid vertices")

    def remove_edge(self,u,v):
        if 0<=u<vertex_count and  0<=v<vertex_count:
            self.adj_list[u]=[(vertex,weight) for vertex,weight in self.adj_list[u] if vertex!=v]
            self.adj_list[v]=[(vertex,weight) for vertex,weight in self.adj_list[v] if vertex!=u]
        else:
            print("Invalid vertices")

    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertx ==v for vertex, x in self.adj_list[u]) 
        else:
            print("Invalid vertices")
            return False
    

    def print_adj_list(self):
        for vertex,n in self.adj_list.items():
            print("V",vertex,":",n)




#####driver codee

g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.print_adj_list()
