def midelement(arr, low, high):
    if low > high:
        return low
 
        
    mid = low + (high-low)//2
    
    if arr[mid] == mid:
        return midelement(arr, mid+1, high)
    else:
        return midelement(arr,low, mid-1)

arr = [0, 1, 2, 6, 7, 8]
low = 0
high = len(arr) - 1
print(midelement(arr, low, high))