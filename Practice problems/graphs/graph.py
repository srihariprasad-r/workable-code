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

 ################################### ################################### ###################################