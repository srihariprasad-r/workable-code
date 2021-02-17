def binarysearch(arr, el, search_first=True):
    n = len(arr)
    end = n - 1
    start = 0
    fso, lso = -1, -1
    while start <= end:
        mid = (end+start)//2
        
        if arr[mid] == el:
            if search_first:
                fso = mid
                end = mid - 1
            else:
                lso = mid
                start = mid + 1
        elif arr[mid] > el:
            end = mid - 1
        else:
            start = mid + 1

    return [fso, lso]

arr = [1, 2, 3, 3, 3, 3, 4, 5]
el = 3
firstoccurance = binarysearch(arr, el)
lastoccurance = binarysearch(arr, el, False)
print(firstoccurance[0], lastoccurance[1])