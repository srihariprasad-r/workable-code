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
        self.previous_value = None
        self.backtrack = {}

    def add_node_graph(self, data, top = None, bottom = None, left = None, right = None):
        self.data = Node(data)
        self.nodes = self.data.add_node(data, top, bottom, left, right)                                  
        self.graph[data] =  self.nodes
        return True
        
    def print_node_edges(self, data):
        for k,v in self.graph.items():
            if k == data:
                return v

    def breadth_first_search(self):
        start_value = 1        
        self.frontier.append(start_value)     
        while self.frontier:
            self.current = self.frontier[0]                     
            node_edges = self.print_node_edges(self.frontier[0])        
            while node_edges['left'] and node_edges['left'] not in self.visited:
                self.frontier.append(node_edges['left'])                    
                break
            while node_edges['right'] and node_edges['right'] not in self.visited:
                self.frontier.append(node_edges['right'])                   
                break                 
            while node_edges['top'] and node_edges['top'] not in self.visited:
                self.frontier.append(node_edges['top'])                   
                break
            while node_edges['bottom'] and node_edges['bottom'] not in self.visited:
                self.frontier.append(node_edges['bottom'])                                                           
                break                                           
            self.visited.append(self.current)                     
            self.frontier.remove(self.current)
        return self.visited

g = Graph()
g.add_node_graph(1, right = 2)
g.add_node_graph(2, left = 1 , right = 3 )
g.add_node_graph(3, left = 2 , right = 4, top = 5, bottom = 7)
g.add_node_graph(4, left = 3)
g.add_node_graph(5, bottom = 3, top = 6 )
g.add_node_graph(6, bottom = 5)
g.add_node_graph(7, bottom = 8 ,  top = 3)
g.add_node_graph(8, top = 7 ,  left = 9, right = 10)
g.add_node_graph(9, right = 8)
g.add_node_graph(10, left = 8)
g.print_node_edges(3)
print(g.breadth_first_search())


