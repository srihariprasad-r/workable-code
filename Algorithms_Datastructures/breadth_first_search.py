"""
x x x x x  x
x x x 6 x  x
x x x 5 x  x 
x 1 2 3 4  x
x x x 7 x  x
x x 9 8 10 x  
x x x x x  x
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.top = None
        self.bottom = None
        self.nodes = {}

    def add_node(self, data, top = None, bottom = None, left = None, right = None):
        self.data = Node(data)
        self.data.left = left
        self.data.right = right
        self.data.top  = top
        self.data.bottom = bottom  
        self.nodes['left'] = self.data.left
        self.nodes['right'] = self.data.right        
        self.nodes['top'] = self.data.top                
        self.nodes['bottom'] = self.data.bottom            
        return self.nodes

class Graph:

    def __init__(self):
        self.graph = {}        
        self.nodes = {}
        self.visited = []
        self.current = None
        self.frontier = []

    def add_node_graph(self, data, top = None, bottom = None, left = None, right = None):
        self.data = Node(data)
        self.nodes = self.data.add_node(data, top, bottom, left, right)                                  
        self.graph[data] =  self.nodes
        return True
        
    def print_node_edges(self, data):
        for k,v in self.graph.items():
            if k == data:
                return v

            
g = Graph()
g.add_node_graph(1)
g.add_node_graph(2, left = 1 , right = 3 )
g.add_node_graph(3, left = 2 , right = 4, top = 5, bottom = 7)
g.add_node_graph(4, left = 3)
g.add_node_graph(5, bottom = 3, top = 6 )
g.add_node_graph(6, bottom = 5)
g.add_node_graph(7, bottom = 8 ,  top = 3)
g.add_node_graph(8, top = 7 ,  left = 9, right = 10)
g.add_node_graph(9, right = 8)
g.add_node_graph(10, left = 8)
print(g.print_node_edges(3))
#g.return_edges(3)


