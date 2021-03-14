class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
class Pair(Node):
    def __init__(self, value, left, right,state=1):
        super().__init__(value, left, right)
        self.state = state


def display(pair):
    if pair is None:
        return
    
    st = ""
    st += str(pair.left.value) if pair.left else "."
    st += " <- " + str(pair.value) + " -> "
    st += str(pair.right.value) if pair.right else "."    
    print(st)
    
    display(pair.left)
    display(pair.right)

def binarytree(arr):
    stck = []
    
    rp = Pair(arr[0], None, None, 1)
    stck.append(rp)
    
    idx = 0
    while len(stck) > 0:
        el = stck[-1]
        if el.state == 1:
            idx += 1
            if arr[idx] != -1:
                el.left = Pair(arr[idx], None, None, 1)
                stck.append(el.left)
            else:
                el.left = None
            el.state += 1
        elif el.state == 2:
            idx += 1
            if arr[idx] != -1:
                el.right = Pair(arr[idx], None, None, 1)
                stck.append(el.right)
            else:
                el.right = None
            el.state += 1
        else:
            stck.pop()
    
    display(rp)

arr = [50,25, -1, -1,12, -1, -1]
print(binarytree(arr))