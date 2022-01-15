def friends_pairing(n):
    def solution(i, n, arr, ans='', res=[]):
        if i > n:
            res.append(ans)
            return
        
        if arr[i]:
            solution(i+1, n, arr, ans, res)
        else:
            arr[i] = True
            solution(i+1, n, arr, ans + "(" + str(i) + ")", res)
            for j in range(i+1, n+1):
                if not arr[j]:
                    arr[j] = True
                    solution(i+1, n, arr, ans + "(" + str(i) + str(j) + ")", res)
                    arr[j] = False
            arr[i] = False
    
        return res
    
    used = [False] * (n+1)
    return solution(1, n, used)

n = 3
print(friends_pairing(n))