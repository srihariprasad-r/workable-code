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

    def find(self, data):
        return self.root.find(self.root,data)

    def get_parent_node(self, data):
        return self.root.get_parent_node(data)

    def is_bst(self):
        return self.root.isBST(self.root)

    def construct_bst_inorder_traversal(self, arr, st, end):
        return self.root.construct_bst_inorder_traversal(arr, st, end)

    def construct_bst_preorder_traversal(self, arr):
        return self.root.construct_bst_preorder_traversal(arr, -float('inf'), float('inf'))

class Node(Tree):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.prev = None
        self.idx = 0
    
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

    def find(self, node, value):
        found = False

        while node:
            if node.data == value:
                found = True
                break
            elif node.data > value:
                node = node.left
            else:
                node = node.right
                    
        return found

    def get_parent_node(self, value):
        parent = None
        
        node = self
        
        while node:
            if node.data < value:
                parent = node
                node = node.right
            elif node.data > value:
                parent = node
                node = node.left
            else:
                break
            
        return parent.data

    def isBST(self, node):
        if node is None:
            return True
            
        if not self.isBST(node.left):
            return False
            
        if self.prev is not None and node.data < self.prev:
            return False
            
        self.prev = node.data
        
        return self.isBST(node.right)

    def construct_bst_inorder_traversal(self, arr, st, end):
        if st > end:
            return None
            
        mid = st + (end - st)//2
        
        new_node = Node(arr[mid])
        
        new_node.left = self.construct_bst_inorder_traversal(arr, st, mid-1)
        new_node.right = self.construct_bst_inorder_traversal(arr, mid+1, end)
        
        return new_node
                
    def construct_bst_preorder_traversal(self, arr, low, high):
        if self.idx >= len(arr) or arr[self.idx] < low or arr[self.idx] > high:
            return None
            
        new_node = Node(arr[self.idx])
        self.idx += 1
        
        new_node.left = self.construct_bst_preorder_traversal(arr, low, new_node.data)
        new_node.right = self.construct_bst_preorder_traversal(arr, new_node.data, high)
        
        return new_node

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
print(bst.find(6))
print(bst.get_parent_node(13))
print(bst.is_bst())
# convert InOrder array into BST
in_order_array = [9,12, 14, 17, 19, 23, 50, 54, 62, 72, 79]
order_array = bst.construct_bst_inorder_traversal(in_order_array, 0, len(in_order_array)-1)
# print newly formed BST in-order traversal
print('New formed BST with In-order traversal...')
order_array.in_order_traversal()
# convert PreOrder array into BST
pre_order_array = [30,20, 10, 15, 25, 23, 39, 35, 42]
pre_order_bst = bst.construct_bst_preorder_traversal(pre_order_array)
# print newly formed BST pre-order traversal
print('New formed BST with Pre-order traversal...')
pre_order_bst.pre_order_traversal()