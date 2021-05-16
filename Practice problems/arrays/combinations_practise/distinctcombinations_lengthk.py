def distinctcombination(arr, k, ans=[], res =[]):
    if k == 0:
        res.append(ans)
        return

    for i in range(len(arr)):
        ch = arr[i]
        distinctcombination(arr[i+1:], k-1, ans+[ch])

    return res
    
arr = [1,2, 3]
print(distinctcombination(arr, 2))