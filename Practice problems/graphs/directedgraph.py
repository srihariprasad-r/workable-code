# below method will implement directed graph using python

class Edge():
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest      

class Graph():
    def __init__(self, numofnodes):
        self.numofnodes = numofnodes
        self.graph = {}     
        self.adjacency_list = [[] for _ in range(numofnodes)]

    def displayEdges(self):
        for node in edgelist:            
            self.adjacency_list[node.src].append(node.dest)
        return self.adjacency_list
        
    def printGraph(self):
        for idx in range(len(self.adjacency_list)):
            for dest in self.adjacency_list[idx]:
                print(f"({idx} -> {dest})" , end= "")
            print()

edgelist = [Edge(3,2) , Edge(2,4), Edge(0,2), Edge(1,3), Edge(3, 0)]
g = Graph(4)
g.displayEdges()
g.printGraph()

