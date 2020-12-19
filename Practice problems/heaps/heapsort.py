def swap(i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
    return 


def heapify(k):
    size = len(array)
    left = 2 * k + 1
    right = 2* k + 2

    smallest  = k

    if left < size and array[left] < array[k]:
        smallest = left 
    elif right < size and array[right] < array[k]:
        smallest = right
    
    if smallest != k:
        swap(k, smallest)
        # heapify(smallest)

array = [6,4,7,1,9,-2]
n = len(array)

i = (n-2) //2 
while i >= 0:
    heapify(i)

print(array)

