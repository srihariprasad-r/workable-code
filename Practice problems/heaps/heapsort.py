def swap(i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
    return array

def heap_sort(arr):
    build_heap(arr)
    print("after build heap:", arr)
    for i in range(len(arr) -1 , 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print("inside for loop:", arr, i)
        heapify(arr,index=0, size=i)

def parent(n):
    return (n-1)//2

def build_heap(arr):
    length = len(arr)
    start = parent(length - 1)
    while start >= 0:
        print("inside loop with start value:", start)
        heapify(arr,index=start, size=length)
        start -= 1

def heapify(arr,index, size):
    left = (2 * index) + 1
    right = (2* index) + 2

    smallest  = index

    if left < size and arr[left] < arr[index]:
        smallest = left 
    
    if right < size and arr[right] < arr[index]:
        smallest = right
    
    print("value is:", smallest, index, left, right)
    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        print("after transpose", arr)
        heapify(arr,smallest, size)


array = [12, 11, 13, 5, 6, 7]
heap_sort(array)

print(array)