def shortestpath(mat, st, end, n, dest_x, dest_y, visited, ans=[], res=[]):
    if st < 0 or st > n or end < 0 or end > n or not(mat[st][end]):
        return False
    
    if st > dest_x or end > dest_y:
        return False

    if st == dest_x and end == dest_y:
        res.append(ans)
        return

    visited[st][end] = True
    if not visited[st+1][end]:
        shortestpath(mat, st+1, end, n, dest_x, dest_y, visited, ans + [(st, end)], res)
    if not visited[st][end+1]:
        shortestpath(mat, st, end+1, n, dest_x, dest_y, visited, ans + [(st, end)], res)
    if not visited[st][end-1]:
        shortestpath(mat, st, end-1, n, dest_x, dest_y, visited, ans + [(st, end)], res)
    if not visited[st-1][end]:
        shortestpath(mat, st-1, end, n, dest_x, dest_y, visited, ans + [(st, end)], res)
    
    visited[st][end] = False
    
    # filter only shortest paths in maze
    f = [res[x] for x in range(len(res)) if len(res[x]) == min(len(res[n]) for n in range(len(res)))]
    
    return f
    
    """
    [[(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (6, 4), (7, 4)], 
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (6, 4), (7, 4)]]
    """

mat = [
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]
src = (0, 0)
dest = (7, 5)
visited = [[False for _ in range(len(mat)+1)] for _ in range(len(mat)+1)]
print(shortestpath(mat, src[0], src[1], 9, dest[0], dest[1], visited))