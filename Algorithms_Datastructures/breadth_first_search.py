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

    def add_node(self, data, top = None, bottom = None, left = None, right = None):
        if self.data == Node(data):
            return 
        else:
            self.data = Node(data)
            if self.top and self.right and self.left and self.bottom:
                self.data.top = Node(top)
                self.data.left = Node(left)
                self.data.right = Node(right)
                self.data.bottom = Node(bottom)                                                
            


