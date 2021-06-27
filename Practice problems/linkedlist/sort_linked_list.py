class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def print_nodes(self):
        head = self
        while head:
            print(head.data)
            head = head.next
            
    def merge(self, node):
        if node is None or node.next is None:
            return node
            
        mid_node = self.middlenode(node)
        secondhalf = mid_node.next
        mid_node.next = None
        
        return self.merge_sort(self.merge(node), self.merge(secondhalf))
            
        
    def middlenode(self, node):
        a = node
        b = node
        
        while b.next and b.next.next:
            a = a.next
            b = b.next.next
        
        return a
        
    def merge_sort(self, l1, l2):
        tmp = Node(-1)
        fnl = tmp
        
        while l1 and l2:
            if l1.data < l2.data:
                tmp.next = l1
                l1 = l1.next
            else:                
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
                
        tmp.next = l1 if l1 else l2
        
        return fnl.next
                
    
head = Node(100)
head = Node(20, head)
head = Node(2, head)
head = Node(25, head)
# head.print_nodes()
nd = head.merge(head)
nd.print_nodes()