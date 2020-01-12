class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class doubly_linked_list:
    def __init__(self):
        self.head = None
    
    def print_linked_list(self):
        cur_node = self.head        
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next        

    def prepend(self,data):
        new_node = Node(data)
        cur_node = self.head
        self.head = new_node
        new_node.next = cur_node
        new_node.prev = None


    def append(self, data):        
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            #print("added new node:", new_node)
            new_node.prev = None
            new_node.next = None
        else:
            new_node = Node(data)
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            
            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = None
        

dll = doubly_linked_list()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.print_linked_list()
#added prepend function
dll.prepend(5)
dll.print_linked_list()
