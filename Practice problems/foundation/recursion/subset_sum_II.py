import copy

def subsetsum(idx, arr, ans=[], res=[]):
    if idx >= len(arr):
        if ans not in res:
            res.append(copy.deepcopy(ans))
        return
    
    for i in range(idx, len(arr)):
        ans.append(arr[i])
        subsetsum(i+1, arr, ans, res)
        ans.pop()
        subsetsum(i+1, arr, ans, res)
        
    return res

arr = [0]
print(subsetsum(0, arr))
# [[1, 2, 2], [1, 2], [1], [2, 2], [2], []]