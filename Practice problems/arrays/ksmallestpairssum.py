def kpairssmallestsum(arr1, arr2,k):
    maxsum = float('inf')
    res = []
    
    for i in range(len(arr1)):
        j = 0
        while j < len(arr2):
            if arr1[i] + arr2[j] < maxsum:
                res.append((arr1[i], arr2[j]))
            j += 1
                
    return sorted(res, key=lambda x : x[0] + x[1])[:k]
                
arr1 = [1, 7, 11]
arr2 = [6, 4, 2]
print(kpairssmallestsum(arr1, arr2, 2))