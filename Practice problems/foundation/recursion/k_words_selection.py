def recursion(idx, s, k='', res=[]):
    if idx > len(s) - 1:
        if k not in res: res.append(k)
        return
    
    for i in range(idx, len(s)):
        recursion(i+1, s, k + s[idx], res)
        recursion(i+1, s, k , res)

    return list(filter(lambda x: x if len(x) == 2 else False, res))
    
s = 'abc'
print(recursion(0, s))
"""
['ab', 'ac', 'bc']
"""
