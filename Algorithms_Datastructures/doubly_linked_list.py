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
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node            
        else:
            new_node = Node(data)   
            cur_node = self.head         
            cur_node.prev = new_node            
            new_node.next = cur_node
            self.head = new_node
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
        
    
    def add_after_node(self, key, data):
        cur_node = self.head
        while cur_node:
            if cur_node.next is None and cur_node.data == key:       #check if key is in head and there is only one element, call append
                self.append(data)
            elif cur_node.data == key:
                new_node = Node(data)
                next_node = cur_node.next
                cur_node.next = new_node
                next_node.prev = new_node
                new_node.next = next_node
                new_node.prev = cur_node
            cur_node = cur_node.next


    def add_before_node(self, key, data):
        cur_node = self.head
        while cur_node:
            if cur_node.next is None and cur_node.data == key:
                self.prepend(data)
            elif cur_node.data == key:
                new_node = Node(data)
                prev_node = cur_node.prev
                new_node.next = cur_node
                new_node.prev = prev_node
                prev_node.next = new_node
            cur_node = cur_node.next

    
    def delete_a_node(self, key):
        cur_node = self.head
        prev_node = Node(key)
        next_node = Node(key)
        while cur_node:
            if cur_node.data == key:
                prev_node = cur_node.prev                
                next_node = cur_node.next                
            cur_node = cur_node.next
        
        next_node.prev = prev_node        
        prev_node.next = next_node


dll = doubly_linked_list()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
#dll.print_linked_list()
#added prepend function
dll.prepend(5)
dll.prepend(9)
#dll.print_linked_list()
#dll.add_after_node(1,30)           # add a node instance after specific list element
#dll.print_linked_list()
#dll.add_before_node(1,30)          # add a node instance before specific list element
#dll.print_linked_list()
dll.delete_a_node(30)               # added function to remove element from doubly linked list
dll.print_linked_list()
