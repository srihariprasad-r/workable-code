def recursion(idx, s, tgt=''):
    if idx < 0:
        return tgt
        
    if idx >= 0:
        tgt = recursion(idx-1, s, tgt + s[idx])

    return tgt
    
s = 'Techie Delight'
print(recursion(len(s)-1, s))