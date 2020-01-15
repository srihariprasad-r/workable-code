class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None        
        self.new_variable = None    
    def insert(self, data):
        if self.value == data:
            return False
        else:
            if self.value > data:
                if self.leftChild:
                    return self.leftChild.insert(data)
                else:
                    self.leftChild = Node(data)                                   
                    return True
            else:
                if self.rightChild:
                    return self.rightChild.insert(data)
                else:
                    self.rightChild = Node(data)
                    return True

    def find(self, data):
        if (self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def lefttraversal(self):
        if self:
            print(self.value)            
            if self.leftChild:
                self.leftChild.lefttraversal()

    def righttraversal(self):
        if self:               
            print(self.value)   
            if self.rightChild:
                self.rightChild.righttraversal()

class Tree:

    def __init__(self):

        self.root = None
    
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:            
            self.root = Node(data)                                      
            return True
    
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def lefttraversal(self):
        return self.root.lefttraversal()

    def righttraversal(self):
        return self.root.righttraversal()

bst = Tree()
print(bst.insert(10))
print(bst.insert(15))
print(bst.insert(8))
print(bst.insert(6))
print(bst.lefttraversal())
print(bst.righttraversal())
