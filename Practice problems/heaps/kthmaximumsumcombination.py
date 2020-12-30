def heap_sort(arr, k):
    build_heap(arr)
    for i in range(len(arr)-1, len(arr)-k , -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

def build_heap(arr):
    n = len(arr)
    for i in range((n//2)-1, -1, -1):
        heapify(arr, i, len(arr)-1)

def heapify(arr, index, size):
    left = 2 * index + 1
    right = 2* index + 2

    if left < size and arr[left] > arr[index]:
        largest = left
    else:
        largest = index

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, size)

def kthmaximumsumcombination(arr1, arr2):
    new_array = []
    for i in range(len(arr1)):
        start = 0
        maxsum = 0
        while start < len(arr1):
            if arr1[i] + arr2[start] > maxsum:
                maxsum = arr1[i] + arr2[start]
                new_array.insert(i,maxsum)
            start += 1
    return new_array

arr1 = [4, 2, 5, 1]
arr2 = [8, 0, 5, 3]
arr = kthmaximumsumcombination(arr1, arr2)
heap_sort(arr, 2)
print(arr)