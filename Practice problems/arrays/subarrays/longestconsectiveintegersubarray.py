def maxlensubarrayconsective(arr):
    mx = -float('inf')
    mn = float('inf')
    mnidx = mxidx = 0
    mxlen = 0
    i = j = 0
    unq_dct = set()
    
    while j < len(arr):
        unq_dct.add(arr[j])
 
        if j - i + 1 < len(unq_dct):
            j += 1
        elif j - i + 1 > len(unq_dct):
            if arr[i] in unq_dct:
                unq_dct.remove(arr[i])
            i += 1
        else:
            mx = -float('inf')
            mn = float('inf')
            
            for k in range(i, j+1):
                mx = max(mx, arr[k])
                mn = min(mn, arr[k])
 
            if mx  - mn + 1 == j - i + 1 and j - i + 1 > mxlen:
                mnidx = i
                mxidx = j
                mxlen = j - i + 1
            else:
                unq_dct.remove(arr[i])
                i += 1
                
            j += 1
            

    return arr[mnidx:mxidx+1]


arr = [2, 5, 6, 2, 4, 3, 1, 0]
print(maxlensubarrayconsective(arr))