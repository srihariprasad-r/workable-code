def binarysearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return low
    
def kclosest(arr, k, x):
    low = 0
    high = len(arr) - 1
    idx = binarysearch(arr, low, high, x)
    
    left = idx - 1
    right = idx
    
    while k > 0:
        if left < 0 or (right < len(arr) and abs(arr[left]-x) > abs(arr[right] -x)):
            right += 1
        else:
            left -= 1
        k -= 1

    return arr[left+1: right]
    

arr = [10, 12, 15, 17, 18, 20, 25]
x = 16
print(kclosest(arr, 4, x))