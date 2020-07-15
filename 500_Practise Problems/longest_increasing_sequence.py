def longestsubsequence(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    tbl = [0 for _ in range(n)] 
    current = 0
    for i in range(m):
        for j in range(m):
            if arr1[i] == arr2[j]:
                if tbl[j] < current + 1:
                    tbl[j] = current + 1
                    #current = tbl[j]

            if (arr1[i] > arr2[j]):
                if tbl[j] > current:
                    #print(arr1[i], arr2[j], tbl[j], current)        
                    current = tbl[j]      

    return max(tbl)

arr1 = [3, 4, 9, 1]
arr2 = [5, 3, 8, 9, 10, 2, 1]

print(longestsubsequence(arr1, arr2))