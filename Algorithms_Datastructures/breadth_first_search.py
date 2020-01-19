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


class Graph:
    def __init__(self):
        self.graph = {}
        self.data = None

    def add_node(self, data, top = None, bottom = None, left = None, right = None):
        self.data = Node(data)
        print("node added:", self.data.data)
        self.data.left = left
        self.data.right = right
        self.data.top  = top
        self.data.bottom = bottom                                     
        return True

    def print_node_edges(self, data):
        print("left node of {0} is : {1}".format(self.data.data, self.data.left))
        print("right node of {0} is : {1}".format(self.data.data, self.data.right))
        print("top node of {0} is : {1}".format(self.data.data, self.data.top))
        print("bottom node of {0} is : {1}".format(self.data.data, self.data.bottom))                        
            
g = Graph()
print(g.add_node(1))
print(g.add_node(2, left = 1 , right = 3 ))
print(g.add_node(3, left = 2 , right = 4, top = 5, bottom = 7 ))
print(g.add_node(4, left = 3))
print(g.add_node(5, bottom = 3, top = 6 ))
print(g.add_node(6, bottom = 5))
print(g.add_node(7, bottom = 8 ,  top = 3))
print(g.add_node(8, top = 7 ,  left = 9, right = 10))
print(g.add_node(9, right = 8))
print(g.add_node(10, left = 8))
g.print_node_edges(10)


