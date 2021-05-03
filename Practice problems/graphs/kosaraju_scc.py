def build_graph(edges, N, visited):
    order = []
    adjlist = {}
    transposed_graph = {}

    for src, dest in edges:
        adjlist.setdefault(src,[]).append(dest)
        transposed_graph.setdefault(dest, []).append(src)

    for i in range(1,N):
        if not visited[i]:
            order = order_dfs(adjlist, i, visited, order)
    
    return order, transposed_graph

def order_dfs(lst, node, visited, order):
    visited[node] = 1

    if node in lst:
        for child in lst[node]:
            if not visited[child]:
                order_dfs(lst, child, visited, order)
    
    order.append(node)

    return order

def transposed_dfs(lst, node, visited, order, scc=[]):
    visited[node] = 1

    if node in lst:
        for child in lst[node]:
            if not visited[child]:
                transposed_dfs(lst, child, visited, order)
    
    scc.append(node)

    return scc

N = 8
edges = [
        (1, 2),
        (2, 3),
        (3, 1),
        (4, 3),
        (7, 4),
        (7, 5),
        (5, 6),
        (6, 7)
    ]
# arrange nodes based on out time of all SCC based on in-degrees
visited = [0] * N
order, transposed_graph = build_graph(edges, N, visited)
# after arranging nodes based on out times, traverse from node with largest out time and do dfs to get SCC
visited = [0] * N
for i in range(1, N):
    if not visited[order[N-1-i]]:
        scc = []
        print('node called for finding SCC..', order[N-1-i])
        scc = transposed_dfs(transposed_graph, order[N-1-i], visited, order)
        for i in range(len(scc)):
            print(scc[i], end=" ")
        print(sep="\n")

################################ Chef and round run ##################################################

def chef_build_graph(val, N, visited):
    order = []
    chef_adjlist = {}
    chef_transposed_graph = {}

    for i in range(N):
         # this is to decide rotation to be made based on val[i]
         # val[i] is 0-index array,  we add 1 to it along with its index and do a modulo with N nodes
         # so, (val[i] + 1 + i) % N gives node which is destination or a cyle which is connected component
        dest = (val[i]+i+1)%N  
        chef_adjlist.setdefault(i, []).append(dest)
        chef_transposed_graph.setdefault(dest,[]).append(i)

    for i in range(1, N):
        if not visited[i-1]:
            order = chef_order_dfs(chef_adjlist, i-1, visited, order)
    
    return order, chef_adjlist, chef_transposed_graph

def chef_order_dfs(lst, node, visited, order):
    if not visited[node]:
        visited[node] = 1
    
    if node in lst:
        for child in lst[node]:
            if not visited[child]:
                chef_order_dfs(lst, child, visited, order)

    order.append(node)

    return order

def chef_scc_dfs(lst, node, visited, scc=[]):
    if not visited[node]:
        visited[node] = 1
    else:
        return 

    if node in lst:
        for child in lst[node]:
            if not visited[child]:
                scc = chef_order_dfs(lst, child, visited, scc)

    scc.append(node)

    return scc

N = 4
A = [1, 1, 1, 1]
visited = [0] * N
order, adj_graph, t_graph = chef_build_graph(A, N, visited)
visited = [0] * N
order_arr = order[::-1]

res = 0

for i in range(1,N+1):
    scc = []
    scc = chef_scc_dfs(t_graph, order_arr[i-1],visited, scc)
     # this condition checks if there is only one node as SCC and if it does not have cycle to itself, its not counted in SCC count 
    if scc and len(scc) == 1 and adj_graph[scc[0]][0] != scc[0]: 
        continue      
    res += 1

print(res)