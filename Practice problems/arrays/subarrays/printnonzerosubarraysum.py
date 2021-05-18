def printnonzerosumsubarray(arr, tgt):
    if len(arr) == 0:
        return
    
    s = {}
    sum = 0
    s.setdefault(0,[]).append(-1)
    al = []
    
    for i in range(len(arr)):
        sum += arr[i]

        # if sum-tgt is seen earlier, possible 0 sum exists
        if sum-tgt in s:
            for val in s[sum-tgt]:
                al.append((val+1, i))
        else:
            s.setdefault(sum,[]).append(i)
        
    # print stored indices
    for i in range(len(al)):
        sindx, eidx = al[i][0], al[i][1]
        print(arr[sindx:eidx+1])

arr = [3, 4, -7, 1, 3, 3, 1, -4]
printnonzerosumsubarray(arr, 7)