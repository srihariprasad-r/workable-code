def recursion(mat, st, end, n, visited, ans='', res=[]):
    if st < 0 or st > n or end < 0 or end > n:
        return False
        
    if st == n and end == n:
        res.append(ans)
        return
    
    if not visited[st+1][end]:
        visited[st][end] = True
        recursion(mat, st+1, end, n, visited, ans + 'D', res)
        visited[st][end] = False
        
    if not visited[st][end+1]:
        visited[st][end] = True
        recursion(mat, st, end+1, n, visited, ans + 'R', res)
        visited[st][end] = False
        
    if not visited[st-1][end]:
        visited[st][end] = True
        recursion(mat, st-1, end, n, visited, ans + 'U', res)
        visited[st][end] = False

    if not visited[st][end-1]:
        visited[st][end] = True
        recursion(mat, st, end-1, n, visited, ans + 'L', res)
        visited[st][end] = False
        
    return res 

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
visited = [[False for _ in range(len(mat[0])+1)] for _ in range(len(mat)+1)]
print(recursion(mat, 0, 0,2, visited))