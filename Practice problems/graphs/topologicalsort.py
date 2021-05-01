from collections import deque

q = deque()
res = []

def build_adjlist(edges, N):
    adjlist = {}
    inDegree = [0] * (N+1)

    for src, dest in edges:
        adjlist.setdefault(src,[]).append(dest) # this is directed graph, so only once we append incoming edges
        inDegree[dest] += 1

    return kahn_algorithm(adjlist, N, inDegree)

def kahn_algorithm(lst, N, inDegree):
    for i in range(1, N+1):
        if inDegree[i] == 0:        # first collect all nodes which has 0 incoming edges(indegree=0)
            q.append(i)
    
    while len(q) > 0:
        el = q.popleft()
        res.append(el)

        if el in lst:
            for child in lst[el]:
                inDegree[child] -= 1        # for those child which has incoming edge from this popped out node, remove the edges
                if inDegree[child] == 0:
                    q.append(child)

    return res

N = 9
edges = [
        (1, 2),
        (3, 4),
        (1, 8),
        (2, 9),
        (2, 5),
        (4, 5),
        (4, 8),
        (5, 9),
        (5, 7),
        (6, 7)
    ]
print(build_adjlist(edges, N))

################################ Implementation example using Priority Queue ##################################################

from queue import PriorityQueue

pq = PriorityQueue()
res = []

def pq_build_adjlist(pq_edges, N):
    pq_adjlist = {}
    pq_inDegree = [0] * (N+1)

    for src, dest in pq_edges:
        pq_adjlist.setdefault(src,[]).append(dest) # this is directed graph, so only once we append incoming edges
        pq_inDegree[dest] += 1

    return pq_kahn_algorithm(pq_adjlist, N, pq_inDegree)

def pq_kahn_algorithm(pq_adjlist, N, pq_inDegree):
    for i in range(1, N+1):
        if pq_inDegree[i] == 0:        # first collect all nodes which has 0 incoming edges(indegree=0)
            pq.put(i)
    
    while not pq.empty():
        el = pq.get()
        res.append(el)

        if el in pq_adjlist:
            for child in pq_adjlist[el]:
                pq_inDegree[child] -= 1        # for those child which has incoming edge from this popped out node, remove the edges
                if pq_inDegree[child] == 0:
                    pq.put(child)

    return res

N = 8
pq_edges = [
        (1, 4),
        (1, 2),
        (4, 2),
        (4, 3),
        (3, 2),
        (5, 2),
        (3, 5),
        (8, 2),
        (8, 6)
    ]
print(pq_build_adjlist(pq_edges, N))