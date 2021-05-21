def minsubarraysumk(arr,k):
    minsum = float('inf')
    i = 0
    j = 0
    start = 0
    end = 0
    cursum = 0
    
    for c in arr:
        cursum += arr[j]
        
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if cursum < minsum:
                minsum = cursum
                start = i
                end = j
            cursum -= arr[i]
            i += 1
            j += 1


    return arr[start: end+1]

arr = [10, 4, 2, 5, 6, 3, 8, 1]
print(minsubarraysumk(arr,3))