def maxsumnonadjacent(arr):
    inclusive_array = [0] * len(arr)
    
    inclusive_array[0] = arr[0]
    inclusive_array[1] = max(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        res = max(inclusive_array[i-1], inclusive_array[i-2] + arr[i])
        inclusive_array[i] = max(res, arr[i])
        
        
    return inclusive_array[-1]
    
arr = [1, 20, 3]
print(maxsumnonadjacent(arr))