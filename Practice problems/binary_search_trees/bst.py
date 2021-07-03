class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            return self.root.insert(data)
            
    def pre_order_traversal(self):
        return self.root.pre_order_traversal()            

    def in_order_traversal(self):
        return self.root.in_order_traversal()

    def post_order_traversal(self):
        return self.root.post_order_traversal()


class Node(Tree):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def insert(self,data):
        new_node = Node(data)
        
        if self is None:
            self = new_node
        else:
            if data < self.data:
                if self.left is None:
                    self.left = new_node
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = new_node
                else:
                    self.right.insert(data)
                    
    def pre_order_traversal(self):
        if self:
            print(self.data)
            if self.left: self.left.pre_order_traversal()
            if self.right: self.right.pre_order_traversal()
            
    def in_order_traversal(self):
        if self:
            if self.left: self.left.in_order_traversal()
            print(self.data)
            if self.right: self.right.in_order_traversal()
            
    def post_order_traversal(self):
        if self:
            if self.left: self.left.post_order_traversal()
            if self.right: self.right.post_order_traversal()
            print(self.data)
 
                
bst = Tree()
bst.insert(8)
bst.insert(3)
bst.insert(6)
bst.insert(10)
bst.insert(4)
bst.insert(7)
bst.insert(1)
bst.insert(14)
bst.insert(13)
print('In-order traversal...')
bst.in_order_traversal()
print('Pre-order traversal...')
bst.pre_order_traversal()
print('Post-order traversal...')
bst.post_order_traversal()