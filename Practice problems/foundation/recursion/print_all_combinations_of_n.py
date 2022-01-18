# needs revisit, only distinct combinations is displayed
def recursion(n, used):
    def solution(idx, n, used, ans=[], res=[]):
        if n == 0:
            res.append(ans)
            return 
        
        if idx > n:
            return
        
        if not used[idx]:
            used[idx] = True
            solution(idx+1, n - idx, used, ans +[idx], res)
            for i in range(idx, n+1):
                if not used[i]:
                    used[i] = True
                    solution(idx+1, n - i, used, ans + [i], res)
                    used[i] = False
            used[idx] = False
        
        return res    
    return solution(1, n, used)

n = 5
used = [False]*(n+1)
print(recursion(n, used)) # [[1,4], [3,2],[5]]