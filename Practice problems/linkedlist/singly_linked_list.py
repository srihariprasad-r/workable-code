class Node():
    def __init__(self, data):
        self.data =  data
        self.next = None
        

class List():
    def __init__(self):
        self.head = None
        
        
    def print_list(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            return
        
        last_node = self.head
            
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = node
        
    def prepend(self, node, data):
        new_node = Node(data)
        
        cur_node = self.head
        prev_node = None
        
        while cur_node and cur_node.data != node:
            prev_node = cur_node
            cur_node = cur_node.next

        if prev_node is None:
            self.head = new_node
            new_node.next = cur_node
        else:
            prev_node.next = new_node
            new_node.next = cur_node
            
    
    def reverse(self):
        cur_node = self.head
        prev_node = None
        
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            
        self.head = prev_node
            

l = List()
l.append('A')
l.append('B')
l.append('C')
l.append('D')
l.prepend('D','E')
l.print_list()
l.reverse()
l.print_list()