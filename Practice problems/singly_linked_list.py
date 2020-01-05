class ListNode:    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        print("current head before prepend:", self.head)
        self.head = ListNode(data=data, next=self.head)
        print("after prepend:", self.head.next)

    def append(self, data):
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
            print("append function , next value:", curr)            
        curr.next = ListNode(data=data)

    def find(self, key):
        curr = self.head
        print("current header", curr)
        while curr and curr.data != key:
            curr = curr.next
            print("find function , next value:", curr)
        return curr  # Will be None if not found

    def remove(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None


lst = SinglyLinkedList()
#lst.prepend(23)
#lst.prepend(53)
#lst.append(23)
print(lst)
#print(lst.find(23))
lst.remove(3)