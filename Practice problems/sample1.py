class A:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class B:
    def __init__(self, head):
        self.head = None
    
    def print_func(self):        
        print(self.next)


b= B(3)
b.print_func()