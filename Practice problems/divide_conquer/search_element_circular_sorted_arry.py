def circularsorted(arr, N, tgt):
    low = 0
    high = len(arr) - 1
    mid = low + (high-low) //2 
    
    while low <= high:
        mid = low + (high-low) //2 

        if arr[low] == tgt:
            return low
        
        nt = (mid + 1) % N
        prv = (mid + N - 1) % N

        if arr[nt] >= arr[mid] and arr[prv] >= arr[mid]:
            return mid
        elif arr[mid] <= tgt:
            high = mid - 1
        elif arr[mid] >= tgt:
            low = mid + 1
            
    return
    
    
arr = [2, 5, 11, 10, 19, 1]
print(circularsorted(arr, 6, 10))