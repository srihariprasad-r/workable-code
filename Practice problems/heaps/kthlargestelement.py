def heap_sort(arr, k):
    build_heap(arr, k)
    for i in range(len(arr)-1, len(arr)-k, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

def build_heap(arr, k):
    # length = len(arr)
    for i in range((len(arr)//2) -1, -1, -1):
        heapify(arr,index=i, size=len(arr))

def heapify(arr, index, size):
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and arr[left] > arr[index]:
        largest = left
    else: 
        largest = index
    
    if right < size and arr[right] > arr[largest]:
        largest = right
    
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr,largest,size)
    
k = 4
array =  [12, 11, 13, 5, 6, 7]
heap_sort(array, k)
print(array[0])