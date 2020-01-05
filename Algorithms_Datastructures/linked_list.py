class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
   
class linkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next        


    def find_next_node(self, data):
        find_node = self.head                
        if find_node.next.data == data:
            return find_node.data , find_node.next


    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return True
        
        last_node = self.head        
        while last_node.next:                                                 
            last_node = last_node.next             
        last_node.next = new_node            


    def insert_after_node(self, pre_node, data):
        _ , previous_node = self.find_next_node(pre_node)        
        inserted_node = Node(data)
        inserted_node.next = previous_node.next        
        previous_node.next = inserted_node
        return True
    """"
        if not pre_node:
            return False
        else:
            new_node = Node(data)
            new_node.next = pre_node.next
            pre_node.next = new_node
    """

    def delete_a_node(self, data):
        node_to_delete = Node(data)
        if node_to_delete is None:
            return False
        else:
            cur_node = self.head  
            prev_node = self.head                  
            while cur_node.next:
                if cur_node.data == data:                    
                    prev_node.next = cur_node.next
                    cur_node.next = None
                else:
                    prev_node = cur_node
                    cur_node = cur_node.next
        
    def reverse_linked_list(self):
        cur_node = self.head
        prev_node = None
        while cur_node:
            next_node = cur_node.next
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node



sll = linkedList()        
sll.append(3)
sll.append(5)
sll.append(6)
sll.prepend(4)
sll.insert_after_node(3,8)
#sll.print_list()
#sll.delete_a_node(5)
#sll.print_list()
sll.reverse_linked_list()
#sll.print_list()