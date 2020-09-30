def msps(arr):
    start = 0
    end = 0

    prd = [i for i in arr]    

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and prd[i] < arr[i] * prd[j]:
                prd[i] = arr[i] * prd[j]
    
    return max(prd)

arr = [3, 100, 4, 5, 150, 6]
print(msps(arr))

