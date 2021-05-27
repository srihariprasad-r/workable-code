def mergesort(A, aux, low, mid, high):
    # segregate the numbers with negatives on left and postives on right
    k = low
    for i in range(low, mid+1):
        if A[i] < 0:
            aux[k] = A[i]
            k += 1

    for i in range(mid+1, high+1):
        if A[i] < 0:
            aux[k] = A[i]
            k += 1

    for i in range(low, mid+1):
        if A[i] >= 0:
            aux[k] = A[i]
            k += 1

    for i in range(mid+1, high+1):
        if A[i] >= 0:
            aux[k] = A[i]
            k += 1
    # sort the seggregated numbers
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

def partition(A, arr,low,high):
    if low == high:
        return
    
    mid = low + (high-low)//2
    
    partition(A, arr, low, mid)
    partition(A, arr, mid+1, high)
    
    mergesort(A, arr, low, mid, high)
    
def get_min_element(arr, low, high):
    if low > high: 
        return low
    
    mid = low + (high-low)//2

    if arr[mid-1] == mid:
        return get_min_element(arr, mid+1, high)
    else:
        return get_min_element(arr, low, mid -1)
        
        
        
arr = [1, 1, 0, -1, -2]
A = arr.copy()
partition(A, arr, 0, len(arr)-1)
# remove elements which are <= 0 since we are needing smallest positive
new_arr = [x for x in arr if x > 0]
print(get_min_element(new_arr, 1, len(new_arr)))