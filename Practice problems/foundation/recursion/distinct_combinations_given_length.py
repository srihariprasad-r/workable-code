def recursion(s,k):
    def solution(idx, s, k, used, ans='', res=[]):
        if len(ans) == k:
            res.append([int(ans[i]) for i in range(len(ans))])
            return
        
        for i in range(idx, len(s)):
            used[i] = True
            solution(idx+1, s, k, used, ans + s[i], res)
            used[i] = False
        
        return res
    
    used = [False for _ in range(len(s))]
    return solution(0, s, k, used)
    
s = '123'
k = 2
print(recursion(s,k)) #    [[1, 2], [1, 3], [2, 2], [2, 3], [3, 2], [3, 3]]