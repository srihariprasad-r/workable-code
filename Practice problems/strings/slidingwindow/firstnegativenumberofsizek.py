def firstnegativenumber(arr,k):
    lst, res = [], []
    i, j = 0, 0
    while j < len(arr):
        if arr[j] < 0:
            lst.append(arr[j])

        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if lst:
                res.append(lst[0])
            else:
                res.append(0)
                
            if lst and arr[i] == lst[0]:
                lst.pop(0)
            i += 1
            j += 1
    return res

arr = [12, -1, -7, 15, -18, 30, 16, 28]
k = 3
print(firstnegativenumber(arr,k))
#[-1, -1, -7, -18, -18, 0]