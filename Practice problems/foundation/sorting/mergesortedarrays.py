def mergesortedarrays(arr1, arr2):
    n = len(arr1) -1 
    m = len(arr2) - 1
    new_arr = []
    i, j, k = 0, 0, 0   # k is pointer for new array
    
    while i <= n and j <= m :
        if arr1[i] < arr2[j]:
            new_arr.insert(k,arr1[i])
            i += 1
            k += 1
        else:
            new_arr.insert(k,arr2[j])
            j += 1
            k += 1
    # below loops will include excess elements in either arrays
    while i < len(arr1):
        new_arr.insert(k,arr1[i])
        i += 1
        k += 1

    while j < len(arr2):
        new_arr.insert(k,arr2[j])
        j += 1
        k += 1        

    return new_arr


arr1 = [1, 2, 5, 8, 9]
arr2 = [3, 4, 6, 7, 10, 11, 12]
print(mergesortedarrays(arr1, arr2))