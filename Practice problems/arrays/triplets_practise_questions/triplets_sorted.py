def sortedtriplet(arr):

    res = []
    
    for i in range(len(arr)-2):
        j = i + 1
        m = len(arr)-1
        while j < m:
            # print(i, j, m)
            if arr[i] < arr[j] and arr[j] < arr[m]:
                res.append((arr[i], arr[j], arr[m]))
                j += 1
            else:
                m -= 1
 
    # O(n2) but pulls all triplets
    # for i in range(len(arr)-2):
    #     for j in range(i+1, len(arr)-1):
    #         m = len(arr)-1 
    #         if arr[i] < arr[j] and arr[j] < arr[m]:
    #             res.append((arr[i],arr[j],arr[m]))
        
    return res
    

arr = [5, 4, 3, 7, 6, 1, 9]
print(sortedtriplet(arr))
            