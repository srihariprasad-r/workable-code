def firstmissingelement(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] < 0 or arr[i] > len(arr):
            continue
        else:
            if arr[i] != i + 1:
                tmp = arr[arr[i] - 1]
                arr[arr[i] - 1] = arr[i]
                arr[i] = tmp
        
    return [i+1 for i in range(len(arr)) if arr[i] != i + 1][:1]


arr = [-2, 11, -3, 1, 3, 4]
print(firstmissingelement(arr))
