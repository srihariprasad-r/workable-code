class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_to_tree(self, data, instruction=None):
        if not self.root:
            self.root = Node(data)
        else:
            return self.root.insert_to_tree(data, instruction)

    def print_nodes(self):
        return self.root.print_nodes()

    def in_order_traversal(self):
        return self.root.in_order_traversal()

    def pre_order_traversal(self):
        return self.root.pre_order_traversal()


class Node(BinaryTree):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        super(BinaryTree, self).__init__()

    def insert_to_tree(self, data, instruction=None):
        if not self.left:
            self.left = Node(data)
        elif not self.right:
            self.right = Node(data)
        elif instruction == 'left':
            self.left.insert_to_tree(data)
        elif instruction == 'right':
            self.right.insert_to_tree(data)

    def print_nodes(self):
        if self:
            print(self.data)
            if self.left:
                self.left.print_nodes()
            if self.right:
                self.right.print_nodes()

    def in_order_traversal(self):
        if self:
            if self.left:
                self.left.in_order_traversal()
            print(self.data)
            if self.right:
                self.right.in_order_traversal()

    def pre_order_traversal(self):
        if self:
            print(self.data)
            if self.left:
                self.left.pre_order_traversal()
            if self.right:
                self.right.pre_order_traversal()


bt = BinaryTree()
bt.insert_to_tree(2)
bt.insert_to_tree(7)
bt.insert_to_tree(5)
bt.insert_to_tree(2, 'left')
bt.insert_to_tree(6, 'right')
bt.insert_to_tree(9, 'left')
# bt.print_nodes()
print('In-order traversal')
bt.in_order_traversal()
print('Pre order traversal')
bt.pre_order_traversal()
