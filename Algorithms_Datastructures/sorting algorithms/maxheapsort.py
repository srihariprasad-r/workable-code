"""
Heapify function - max heap
Input = [1,3,2,4,9,7,5]

     1
    /  \
  3     2
 / \    / \
4   9   7  5

"""

def elementsize(array):
    size = len(array)
    #array.insert(0,1)
    return size

def findparent(array, index):
    parent = (index //2)
    leftnode = 2* index
    rightnode = 2*index + 1
    #print(parent, leftnode, rightnode)
    return leftnode, rightnode

def findswap(array, index1, index2):
    tmp = array[index1]
    array[index1] = array[index2]
    array[index2] = tmp
    return True

def findlargestnode(array, index, size = 0):
    l, r = findparent(array, index)
    largest = index
    if size > l and array[l] > array[index] :
        largest = l
    if size > r and array[r] > array[largest]:
        largest = r
    if largest != index:
        findswap(array, index, largest)
        findlargestnode(array, largest, size)
    return array

array = [0,1,3,2,4,9,7,5]
#p, l, r = findparent(3)
#print(p,l,r)
#findswap(2,3)
size = elementsize(array)
sortedarray = findlargestnode(array, 1, size)
print(sortedarray)


#print(sortedarray)