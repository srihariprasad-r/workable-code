def printallsubarraywithgivensum(arr,k):
    cursum = 0
    i = j = 0
    start = end = 0
    res = []
    
    while j < len(arr):
        cursum += arr[j]
        
        if cursum < k:
            j += 1
        elif cursum == k:
            start = i
            end = j
            res.append((start, end))
            cursum -= arr[i]
            i += 1
            j += 1
        else:
            
            while cursum > k:
                cursum -= arr[i]
                i += 1
                if cursum == k:
                    res.append((i, j))
            j += 1

    for i in range(len(res)):
        sidx, eidx = res[i][0], res[i][1]
        print(arr[sidx:eidx+1])
    
    
arr =[2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
k = 15
print(printallsubarraywithgivensum(arr,k))