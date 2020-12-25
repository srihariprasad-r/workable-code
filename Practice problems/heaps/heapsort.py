def swap(i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
    return array

def heap_sort(arr):
    build_heap(arr)
    for i in range(len(arr) -1 , -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, len(arr)-1)

def build_heap(arr):
    length = len(arr) -1
    for i in range((len(arr)//2)-1, -1, -1):
        heapify(arr,index=i, size=length)

def heapify(arr,index, size):
    left = (2 * index) + 1
    right = (2* index) + 2

    if left <= size and arr[left] > arr[index]:
        smallest = left 
    else:
        smallest = index
    
    if right <= size and arr[right] > arr[smallest]:
        smallest = right
    
    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        heapify(arr,smallest, size)


array = [12, 11, 13, 5, 6, 7]
heap_sort(array)

print(array)