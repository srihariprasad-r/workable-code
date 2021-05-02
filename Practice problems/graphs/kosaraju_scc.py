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
