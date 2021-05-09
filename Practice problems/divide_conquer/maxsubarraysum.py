def maxsumsubarray(A, low, high):

    if low == high:
        return arr[low]
        
    mid = low + (high - low)//2
    
    leftmaxsum = -float('inf')
    csum = 0
    for i in range(mid, low-1, -1):
        csum += A[i]
        if leftmaxsum < csum:
            leftmaxsum = csum
    
    
    rightmaxsum = -float('inf')
    csum = 0
    for i in range(mid+ 1, high+1):
        csum += A[i]
        if rightmaxsum < csum:
            rightmaxsum = csum
            
    maxsum = max(maxsumsubarray(arr, low, mid), maxsumsubarray(arr, mid+1, high))

    return max(maxsum, leftmaxsum+ rightmaxsum)
    
arr = [2, -4, 1, 9, -6, 7, -3]
print(maxsumsubarray(arr, 0, len(arr)-1))