def longestconsectivesubarray(arr):
    if len(arr) == 0:
        return
    elif len(arr) == 1:
        return arr[0]
    
    mx = -float('inf')
    mn = float('inf')
    mxi = 0
    mxj = 0
    uq_set = set()    
    i = 0
    j = 0
    
    for c in arr:
        uq_set.add(c)
        
        if j - i + 1 == len(uq_set):
            for k in range(i, j +1):
                if mx < arr[k]:
                    mx = arr[k]
                if mn > arr[k]:
                    mn = arr[k]

            if mx - mn + 1 == j - i + 1:
                mxi = i
                mxj = j

            j += 1
        elif j - i + 1 > len(uq_set):
            while i == j:
                uq_set.remove(arr[i])
                i += 1
            i += 1
            j += 1
        else:
            j += 1
                
    return arr[mxi:mxj + 1]
            
arr = [2, 5, 6, 2, 4, 3, 1, 0]
print(longestconsectivesubarray(arr))