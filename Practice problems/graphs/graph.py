################## Implements Depth first search ###################################
res = []

def build_graph(edges, N):
    graph = {}
    for src, dest in edges:
        graph.setdefault(src,[]).append(dest)
        graph.setdefault(dest,[]).append(src)

    return dfs(graph, 'A', res)


def dfs(adjlist, vertex, res = []):
    if vertex not in res : 
        res.append(vertex)
 
        if vertex not in adjlist:
            return res
        else:
            for n in adjlist[vertex]:
                res = dfs(adjlist, n, res)
    return res

N = 7
edges = [
        ('A', 'B'),
        ('A','C'),
        ('B','D'),
        ('B','E'),
        ('C', 'F'),
        ('E','F')
    ]
returned_list = build_graph(edges, N)
print(res)  # ['A', 'B', 'D', 'E', 'F', 'C']

 ################################### Find strongly connected_components ###################################

res = []

def connected_components_build_graph(edges, N):
    connected_count = 0
    nodes = ['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'M', 'N', 'O']
    graph = {}
    for src, dest in edges:
        graph.setdefault(src,[]).append(dest)
        graph.setdefault(dest,[]).append(src)
    
    for i in range(len(nodes)):
        if nodes[i] not in res: connected_count += 1
        _ = connected_components_dfs(graph, nodes[i], res)
    return connected_count

def connected_components_dfs(adjlist, vertex, res = []):
    if vertex not in res : 
        res.append(vertex)
 
        if vertex not in adjlist:
            return res
        else:
            for n in adjlist[vertex]:
                res = dfs(adjlist, n, res)
    return res

N = 12
edges = [
        ('A', 'B'),
        ('A','C'),
        ('B','D'),
        ('B','E'),
        ('C', 'F'),
        ('E','F'),
        ('G', 'H'),
        ('M','N'),
        ('N','O')
    ]
connected_component_count = connected_components_build_graph(edges, N)
print(connected_component_count)    # 3

 ################################ Bipartite graph ##################################################

def bipartite_build_graph(edges, N):
    graph = {}
    visited = [0]*N
    color = [0]*N 
    
    for src, dest in edges:
        graph.setdefault(src, []).append(dest)
        graph.setdefault(dest, []).append(src)

    for i in range(N):
        if visited[0] == 0:
            return bipartite_check(graph, 'A', visited, color, 0)
    
def bipartite_check(graph, nodes, visited, color, c):
    visited[ord(nodes)-ord('A')] = 1
    color[ord(nodes)-ord('A')] = c

    for child in graph[nodes]:
        for i in range(len(child)):
            if visited[ord(child[i]) - ord('A')] == 0:
                bipartite_check(graph, child[i], visited, color, c ^ 1)
            else:
                if color[ord(nodes)-ord('A')] == color[ord(child[i]) - ord('A')]:
                    return False

N = 6
edges = [
        ('A', 'B'),
        ('A','C'),
        ('B','D'),
        ('B','E'),
        ('C', 'F'),
        ('E','F')
    ]
print(bipartite_build_graph(edges, N))