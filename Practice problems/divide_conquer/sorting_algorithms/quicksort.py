def quicksort(arr, low, high):
    pivot = arr[high]
    
    idx = low
    
    for i in range(low, high):
        if arr[i] <= pivot:
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp
            idx += 1
    
    tmp = arr[high]
    arr[high] = arr[idx]
    arr[idx] = tmp

    return idx
        

def partition(arr, low, high):
    if low >= high:
        return low
   
    mid = quicksort(arr, low, high)
    
    partition(arr, low, mid-1)
    partition(arr, mid+1, high)
    
    return arr

arr = [2, 3, 4, 1, 8, 6, 7, 5]
print(partition(arr, 0, len(arr)-1))