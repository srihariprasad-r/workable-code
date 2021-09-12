class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_to_tree(self, data, parent=None, instruction=None):
        if not self.root:
            self.root = Node(data)
        else:
            return self.root.insert_to_tree(data, parent, instruction)

    def print_nodes(self):
        return self.root.print_nodes()

    def in_order_traversal(self):
        return self.root.in_order_traversal()

    def pre_order_traversal(self):
        return self.root.pre_order_traversal()

    def print_left_view_binary_tree(self):
        return self.root.print_left_view_binary_tree(node=self.root)


class Node(BinaryTree):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        super(BinaryTree, self).__init__()

    def insert_to_tree(self, data, parent=None, instruction=None):
        if not self.left:
            self.left = Node(data)
        elif not self.right:
            self.right = Node(data)
        elif instruction == 'left':
            head = self

            while parent != head.data:
                if parent == self.left.data:
                    head = self.left
                else:
                    head = self.right
            head.left = Node(data)
        elif instruction == 'right':
            head = self

            while parent != head.data:
                if parent == self.right.data:
                    head = self.right
                else:
                    head = self.left
            head.right = Node(data)
            # self.right.insert_to_tree(data)

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

    def print_left_view_binary_tree(self, node=None, level=0, maxlevel=0, hash_map={}):
        if node is None:
            return

        if level not in hash_map:
            hash_map[level] = node.data
            level += 1

        self.print_left_view_binary_tree(node.left, level, hash_map)
        self.print_left_view_binary_tree(node.right, level, hash_map)

        return [k for k in hash_map.values()]


bt = BinaryTree()
bt.insert_to_tree(2)
bt.insert_to_tree(7)
bt.insert_to_tree(5)
bt.insert_to_tree(2, 7, 'left')
bt.insert_to_tree(6, 7, 'right')
bt.insert_to_tree(9, 5, 'right')
# bt.print_nodes()
# print('In-order traversal')
# bt.in_order_traversal()
# print('Pre order traversal')
#bt.pre_order_traversal()
print(bt.print_left_view_binary_tree())
