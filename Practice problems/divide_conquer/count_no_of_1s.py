def binarysearch(arr, low, high):
    if arr[high] == 0:
        return 0
        
    if arr[low] == 1:
        return high-low + 1
    
    mid = low + (high-low)//2
    
    return binarysearch(arr, low, mid) + binarysearch(arr, mid+1, high)

arr = [0, 0, 0, 1, 1, 1]
print(binarysearch(arr, 0, len(arr)-1))
