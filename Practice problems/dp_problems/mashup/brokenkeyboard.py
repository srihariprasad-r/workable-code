def brokenkeyboard(str, k):
    n = len(str)
    typeable = [False] * (26)
    a = [0] * len(str)
    f = [0] * (len(str)+1)
    ans = 0
    
    for i in k:
        typeable[ord(i) - ord('a')] = True
        
    for i in range(len(str)):
        if typeable[ord(str[i])- ord('a')]:
            a[i] = 1
        else:
            a[i] = 0
            
    f[0] = 0
    for i in range(n):
        if a[i]:
            f[i+1] = f[i] + 1
        else:
            f[i+1] = 0
            
        ans += f[i+1]
    
    return ans
    
str = 'abacaba'
k = ['a', 'b']
print(brokenkeyboard(str, k))
