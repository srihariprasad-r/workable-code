def maxsumsubarray(arr):
    maxsum = -float('inf')
    
    start = 0
    end = 0
    
    for i in range(len(arr)):
        j = i + 1
        cursum = arr[i]
        while j < len(arr):
            cursum += arr[j]
            if cursum > maxsum:
                maxsum = cursum
                start = i
                end = j
            j += 1
            
    return arr[start:end+1]
    
arr = [8, -7, -3, 5, 6, -2, 3, -4, 2]
print(maxsumsubarray(arr))