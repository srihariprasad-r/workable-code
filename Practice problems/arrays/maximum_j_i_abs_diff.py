def max_j_i(arr):
    stck = []
    res = []
    
    for i in range(len(arr)):
        j = i + 1
        while j < len(arr):
            if arr[i] < arr[j]:
                if not stck:
                    stck.append((i,j))
                else:
                    idx = stck[-1][1]
                    if arr[i] < arr[idx] and j > idx:
                        stck.pop()
                        stck.append((i,j))
            j += 1
        
    return stck[-1][1] - stck[-1][0] if stck else -1 

arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
print(max_j_i(arr))