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
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node            
        self.head = prev_node                


    def merge_two_list(self, list2):
        node1 = self.head
        node2 = list2.head
        index_node = None

        if node1 is None:
            return node2
        elif node2 is None:
            return node1

        if node1 and node2:
            if node1.data <= node2.data:
                index_node = node1
                node1 = index_node.next     #moved the node to point to next element from head
            else:
                index_node = node2    
                node2 = index_node.next
            
            new_head = index_node   #set head to newly added node

        while node1 and node2:
            if node1.data <= node2.data:
                index_node.next = node1
                index_node = node1
                node1 = index_node.next
            else:
                index_node.next = node2
                index_node = node2
                node2 = index_node.next   

        if node1 is None:
            index_node.next = node2
        elif node2 is None:
            index_node.next = node1 

        return new_head                            



sll1 = linkedList()        
sll2 = linkedList()

#add elements to first linked list object
sll1.append(4)
sll1.append(5)
sll1.append(6)
sll1.prepend(3)


#add elements to second linked list object
sll2.append(1)
sll2.append(2)
sll2.append(7)
sll2.append(8)

sll1.merge_two_list(sll2)                           #need validation
sll1.print_list()
#sll.insert_after_node(3,8)                         #inserts node after node that is passed
#sll.print_list()
#sll.delete_a_node(5)                               #removes a node
#sll.print_list()
#sll.reverse_linked_list()                          #reverses linked list
#sll.print_list()