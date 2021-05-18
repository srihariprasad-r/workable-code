def printzerosumsubarray(arr):
    if len(arr) == 0:
        return
    
    s = {}
    sum = 0
    s.setdefault(0,[]).append(-1)       # default value to accomodate 0 at index 1
    al = []
    
    for i in range(len(arr)):
        sum += arr[i]
        # if sum is seen earlier, possible 0 sum exists
        if sum in s:
            for val in s[sum]:
                al.append((val+1, i))
        else:
            s.setdefault(sum,[]).append(i)
        
    # print stored indices
    for i in range(len(al)):
        sindx, eidx = al[i][0], al[i][1]
        print(arr[sindx:eidx+1])

arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
printzerosumsubarray(arr)