def tripletsumlessthanK(arr, k):
    arr.sort()
    diff_sum = 0
    res = []
    
    for i in range(len(arr)-2):
        diff_sum = k - arr[i]
        j = i + 1
        m = len(arr)-1
        while j < m:
            if arr[j] + arr[m] <= diff_sum:
                res.append((arr[i], arr[j], arr[m]))
                j += 1
            else:
                m -= 1

    
    return res
        
arr = [ 2, 7, 4, 9, 5, 1, 3 ]
print(tripletsumlessthanK(arr, 10))