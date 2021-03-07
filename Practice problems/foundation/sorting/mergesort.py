def mergesort(arr, low=0, high=0):
    if low == high:
        ba = [arr[low]]
        return ba
        
    mid = (low + high)//2
    arr1 = mergesort(arr, low, mid)
    arr2 = mergesort(arr, mid+1, high)
    arr = mergesortedarrays(arr1, arr2)
    return arr
    
    
def mergesortedarrays(arr1, arr2):
    n = len(arr1) -1 
    m = len(arr2) - 1
    new_arr = []
    i, j, k = 0, 0, 0
    
    while i <= n and j <= m :
        if arr1[i] < arr2[j]:
            new_arr.insert(k,arr1[i])
            i += 1
            k += 1
        else:
            new_arr.insert(k,arr2[j])
            j += 1
            k += 1
 
    while i < len(arr1):
        new_arr.insert(k,arr1[i])
        i += 1
        k += 1

    while j < len(arr2):
        new_arr.insert(k,arr2[j])
        j += 1
        k += 1        

    return new_arr


arr = [1, 2, 5, 8, 9, 3, 4, 6, 7, 10, 11, 12]
print(mergesort(arr, 0, len(arr)-1))