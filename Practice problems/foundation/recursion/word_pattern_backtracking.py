import copy 
def recursion(str, ptn, map={}, res=[]):
    if len(ptn) == 0:
        if len(str) == 0:
            res.append(copy.deepcopy(map))
            return
        else:
            return
    
    ch = ptn[0]
    rop = ptn[1:]
    
    if ch in map:
        if map[ch] == str[0:len(map[ch])]:
            recursion(str[len(map[ch]):], rop, map, res)
    else:
        for i in range(len(str)):
            prefix = str[0:i+1]
            rest = str[i+1:]
            map[ch] = prefix
            recursion(rest, rop, map, res)
            del map[ch]
        
    return res

s = 'graphtreesgraph'
p = 'pep'
print(recursion(s, p))
"""
[{'p': 'graph', 'e': 'trees'}]
"""