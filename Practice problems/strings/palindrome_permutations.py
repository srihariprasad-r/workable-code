def permutation(s,ans='', res=[]):
    if len(s) == 0:
        if ans not in res: res.append(ans)
    
    for i in range(len(s)):
        ch = s[i]
        left = s[0:i]
        right = s[i+1:]
        permutation(left+right, ch + ans, res)
    
    return res

def check_palindrome(s):
    low = 0
    high = len(s) - 1
    
    while  low < high:
        if s[low] != s[high]:
            return False
            
        low += 1
        high -= 1
    
    return True
    
s = 'radar'
ot = permutation(s)
ps = set()
for i in range(len(ot)):
    if check_palindrome(ot[i]):
        ps.add(ot[i])
        
print(ps)