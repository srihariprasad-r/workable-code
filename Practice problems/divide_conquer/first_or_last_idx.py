def findfirstorlastidx(arr, N, tgt):
    low = 0
    high = len(arr) - 1
    mid = low + (high-low) //2 
    
    while low <= high:
        mid = low + (high-low) //2 
        if arr[low] == tgt or arr[high] == tgt:
            return low if arr[low] == tgt else high
        elif arr[mid] <= tgt:
            low = mid + 1
        elif arr[mid] >= tgt:
            high = mid - 1
            
    return
    
    
arr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
print(findfirstorlastidx(arr, 10, 5))