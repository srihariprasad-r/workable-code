import copy

def recursion(idx, s, n, tsets, k, res=[]):
    if n == idx :
        k = [k[x] for x in range(len(k)) if len(k[x]) > 0]
        if k not in res: res.append(copy.deepcopy(k))
        return
    
    if idx > n - 1:
        return
    
    for i in range(len(k)):
        if len(k[i]) == 0:
            k[i].append(s[idx])
            recursion(idx+1, s, n, tsets + 1, k, res)
            k[i].pop()
        else:
            k[i].append(s[idx])
            recursion(idx+1, s, n, tsets, k, res)
            k[i].pop()
    
    return res


s = 'ABC'
k=[[] for _ in range(len(s))]
print(recursion(0, s, len(s), 0, k))
"""
[[['A', 'B', 'C']], 
[['A', 'B'], ['C']], 
[['A', 'C'], ['B']], 
[['A'], ['B', 'C']], 
[['A'], ['B'], ['C']], 
[['A'], ['C'], ['B']], 
[['B', 'C'], ['A']], 
[['B'], ['A', 'C']], 
[['B'], ['A'], ['C']], 
[['C'], ['A', 'B']], 
[['C'], ['A'], ['B']], 
[['B'], ['C'], ['A']], 
[['C'], ['B'], ['A']]]
"""