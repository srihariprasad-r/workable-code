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
        else:
            if instruction:
                if instruction == 'left':
                    self.left = Node(data)
                else:
                    self.right = Node(data)

    def print_nodes(self):
        if self:
            print(self.data)
            if self.left:
                self.left.print_nodes()
            if self.right:
                self.right.print_nodes()


bt = BinaryTree()
bt.insert_to_tree(2)
bt.insert_to_tree(7)
bt.insert_to_tree(6)
bt.print_nodes()