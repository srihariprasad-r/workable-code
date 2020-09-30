def msis(arr):
    start = 0
    end = 0

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and arr[i] < arr[i] + arr[j]:
                end = i
            else:
                start = i+1
    
    return len(arr[start: end + 1 ])

arr = [3,2, 4,5,10]
print(msis(arr))

