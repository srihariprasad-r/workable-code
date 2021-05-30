def longestconsectivesubsequence(arr):
    v = set()
    mx = 0
    v= {x for x in arr}
    
    res = {}
    
    for i in range(len(arr)):
        if not(arr[i]-1 in v):
            cnt = 1

            while cnt + arr[i] in v:
                res.setdefault(arr[i],[]).append(arr[i]+cnt)
                cnt += 1
                
            mx = max(mx, cnt)
    
    return mx

arr = [2, 0, 6, 1, 5, 3, 7]
print(longestconsectivesubsequence(arr))