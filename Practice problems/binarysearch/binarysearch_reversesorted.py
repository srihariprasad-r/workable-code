def binarysearch(arr, el):
    n = len(arr)
    end = n - 1
    start = 0
    
    while start <= end:
        mid = (end+start)//2
        
        if arr[mid] == el:
            return mid
        elif arr[mid] < el:
            end = mid - 1
        else:
            start = mid + 1

    return -1

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
el = 2
print(binarysearch(arr, el))