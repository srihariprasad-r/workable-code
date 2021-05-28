def increasingsubeqofklengthmaxproduct(arr):
    lstck = []
    rstck = []
    res = []
    prodmaxsum = 1
    
    for i in range(len(arr)-1):
        j = i + 1
        while j < len(arr):
            if arr[i] < arr[j]:
                if not lstck:
                    lstck.append((i,j))
                else:
                    el1, el2 = lstck[-1][0], lstck[-1][1]
                    if arr[i] * arr[j] > arr[el1] * arr[el2] and arr[i] * arr[j] > prodmaxsum:
                        prodmaxsum = arr[i] * arr[j]
                        lstck.pop()
                        lstck.append((i,j))
            j += 1
            
    minidx = lstck[-1][0]
    j = 0
    
    while j < minidx:
        if arr[j] < arr[minidx]:
            if not rstck: rstck.append(j)
            else:
                el = rstck[-1]
                if arr[el] < arr[j]:
                    rstck.pop()
                    rstck.append(j)
        j += 1
    
    return (arr[rstck[-1]], arr[lstck[-1][0]], arr[lstck[-1][1]])
            
        
arr = [1, 5, 10, 8, 9]
print(increasingsubeqofklengthmaxproduct(arr))
