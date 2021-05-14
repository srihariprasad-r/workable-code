def binarysearch(arr, tgt, searchleft):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high - low)//2
        
        if arr[mid] == tgt:
            cnt = mid
            if searchleft:
                high = mid - 1
            else:
                low = mid + 1
        elif arr[mid] > tgt:
            high = mid -1
        else:
            low = mid + 1
    
    return cnt
        

arr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
tgt = 5

low = binarysearch(arr, tgt, True)
high = binarysearch(arr, tgt, False)
print(high - low + 1)