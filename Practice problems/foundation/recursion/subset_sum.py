import copy

def subsetsum(idx, arr, ans=[], res=[]):
    if idx >= len(arr):
        if ans not in res:
            res.append(copy.deepcopy(ans))
        return
    
    for i in range(idx, len(arr)):
        subsetsum(i+1, arr, ans + [arr[i]], res)
        subsetsum(i+1, arr, ans, res)
        
    return sorted([sum(res[i]) for i in range(len(res))])

arr = [3, 1, 2]
print(subsetsum(0, arr))
# [0, 1, 2, 3, 3, 4, 5, 6]
