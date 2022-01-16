def recursion(n, k):
    def solution(idx, n, k, totalsets, used):
        if idx > n:
            if k == totalsets:
                print(used)
            return
 
        for i in range(len(used)):
            curr_set = used[i]
            if len(used[i]) > 0:
                used[i].append(idx)
                solution(idx+1, n, k, totalsets, used)
                used[i].pop()
            else:
                used[i].append(idx)
                solution(idx+1, n, k, totalsets+1, used)
                used[i].pop()
                break
        return
        
    used = [[] for _ in range(k)]
    return solution(1, n, k, 0, used)

recursion(3, 2)