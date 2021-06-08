def split_array(arr, low, high):
    if low > high:
        return

    if high - low == 1:
        return
    
    mid = low + (high - low) // 2
    
    temp = mid + 1
    
    mmid = low + (mid- low) // 2
    
    for i in range(mmid+1, mid+1):
        arr[i], arr[temp] = arr[temp], arr[i]
        temp += 1
    
    split_array(arr, low, mid)
    split_array(arr,mid + 1, high)
    
    return arr

arr = [1, 3, 5, 7, 2, 4, 6, 8]
print(split_array(arr, 0, len(arr)-1))