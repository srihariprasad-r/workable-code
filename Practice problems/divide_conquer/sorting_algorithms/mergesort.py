def merge(A,arr, low, mid, high):
    k = low
    i = low
    j = mid + 1
    
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            arr[k] = A[i]
            i += 1
            k += 1
        else:
            arr[k] = A[j]
            j += 1
            k += 1
            
    while i <= mid:
        arr[k] = A[i]
        i += 1
        k += 1
        
    while j <= high:
        arr[k] = A[j]
        j += 1  
        k += 1
    
    for i in range(low, high+1):
        A[i] = arr[i]
        

def partition(A, arr, low, high):
    if low == high:
        return low
    mid = low + (high - low)//2 
    
    partition(A, arr, low, mid)
    partition(A,arr, mid+1, high)

    merge(A,arr, low, mid, high)
    
    return A

arr = [2, 3, 4, 1, 5, 6, 7, 8]
A = arr.copy()
print(partition(A, arr, 0, len(arr)-1))