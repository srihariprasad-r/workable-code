"""

Pre-order : NLR (L-> left; N-> Node ; R -> Right)
In-order : LNR
Post-order: LRN

        50
       /  \
      25   75
     / \   /  \
    12 37  62  87

           N     N  L  R    N  L  R
           N  |  L  L  L |  R  R  R
Pre-order: 50 | 25 12 37 | 75 62 87

            L  N  R   N     L  N  R
            L  L  L | N  |  R  R  R
In-order:  12 25 37 | 50 | 62 75 87


            L  R  N    L  R  N  | N
            L  L  L  | R  R  R  | N
Post-order: 12 37 25 | 62 87 75 | 50
"""
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
    print("#============== BEGIN =================================#")
    print("#========Display of tree elements with nodes ==========#")
    display(rp)
    print("#========Pre/post & In order traversal ================#")
    traversal(rp)
    print("#========Level order traversal ========================#")
    levelorder(rp)
    print("#========Find path from node to root ========================#")
    findelement(rp, 70)
    print(path)
    print("#========Print K levels down ========================#")
    printKlevels(rp, 3)
    print("#========Print K levels far from the node ================#")
    printnodesKlevelsfar(rp, 40, 3)
    print("#=================END =================================#")
    
def traversal(pair):
    if pair is None:
        return
    
    print(str(pair.value) + " pre-order ")
    traversal(pair.left)
    print(str(pair.value) + " in-order ")
    traversal(pair.right)
    print(str(pair.value) + " post-order ")


def levelorder(pair):
    from collections import deque
    q =deque()

    q.append(pair)

    while len(q) > 0:
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            print(str(node.value) + " ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

path = []
def findelement(pair, data):
    if pair is None:
        return False
        
    if pair.value == data:
        path.append(pair.value)
        return True
    
    if pair.left:
        filc = findelement(pair.left, data)
        if filc:
            path.append(pair.value)
            return True
            
    if pair.right:
        firc = findelement(pair.right, data)
        if firc:
            path.append(pair.value)
            return True
            
    return False

def printKlevels(pair,k):
    if pair is None or k < 0:
        return
    
    if k == 0:
        print(pair.value)
        
    printKlevels(pair.left, k-1)
    printKlevels(pair.right, k - 1)
    
rootpath = []    
def printnodesKlevelsfar(pair, data, k):
    def find(pair, data):
        if pair is None:
            return False
        
        if pair.value == data:
            rootpath.append(pair)
            return True
    
        filc = find(pair.left, data)
        if filc:
            rootpath.append(pair)
            return True
    
        firc = find(pair.right, data)
        if firc:
            rootpath.append(pair)
            return True
        
        return False
    
    def _printKlevels(pair, k, blocker):
        if pair is None or k < 0 or pair == blocker:
            return
        if k == 0:
            print(pair.value)
        _printKlevels(pair.left, k - 1, blocker)
        _printKlevels(pair.right, k - 1, blocker)
        
    find(pair, data)
    for i in range(len(rootpath)):
        _printKlevels(rootpath[i], k-i, None if i == 0 else rootpath[i-1])


arr = [50,25,12, -1, -1, 37, 30, -1, -1, 40, -1, -1, 75, 62, 60, -1, -1, 70, -1, -1, 87, -1, -1]
print(binarytree(arr))