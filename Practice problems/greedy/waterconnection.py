def waterConnection(n, p, a, b, d, ans=[]):
    def dfs(graph, start, end, weight, visited):

        visited[end] = 1
        
        if end in graph:
            nextnode, w = graph[end]
            if visited[nextnode] == 0:
                visited[nextnode] = 1
                min_weight = min(weight, w)
                return dfs(graph, start, nextnode, min_weight, visited)
        else:
            return end, weight
        
    graph = {}
    visited = [0] * (n+1)
    out_pipe = [0] * (n+1)
    in_pipe = [0] * (n+1)
  
    for i in range(p):
        graph[a[i]] = [b[i], d[i]]
        out_pipe[a[i]] = 1
        in_pipe[b[i]] = 1

    for j in range(1, n+1):
        if in_pipe[j] == 0 and out_pipe[j] == 1 and visited[j] == 0:
            start = j
            end, weight = dfs(graph, j, j, float('inf'), visited)
            ans.append((start, end, weight))
            
    return ans

n = 9
p = 6
a = [7,5,4,2,9,3]
b = [4,9,6,8,7,1]
d = [98,72,10,22,17,66]

print(waterConnection(n, p, a, b, d))