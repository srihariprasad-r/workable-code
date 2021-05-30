def longestincreasingconsectivesubsequence(arr):
    res = {}
    mx = 0
    for i in range(len(arr)):
        j = i + 1
        diff = 0
        if arr[i] not in res:
            while j < len(arr):
                if arr[j] - arr[i]  ==  diff + 1:
                    diff = arr[j] - arr[i]
                    res.setdefault(arr[i],[]).append(arr[j])
                    mx = max(mx, len(res[arr[i]]))
                j += 1
    
    return mx + 1
            

arr = [6, 7, 8, 3, 4, 5, 9, 10]
print(longestincreasingconsectivesubsequence(arr))