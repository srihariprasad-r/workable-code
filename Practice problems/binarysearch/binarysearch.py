def binarysearch(arr, el):
    n = len(arr)
    end = n - 1
    start = 0
    
    while start <= end:
        mid = (end+start)//2
        
        if arr[mid] == el:
            return mid
        elif arr[mid] > el:
            end = mid - 1
        else:
            start = mid + 1

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
el = 10
print(binarysearch(arr, el))