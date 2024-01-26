# cycle in DAG
import collections

edges = [(1,2),(8,2),(8,9),(9,10),(10, 8), (2,3),(3,7),(3,4),(7,5),(4,5),(5,6)]

lst = collections.defaultdict(list)
visited = [0]*11
path = [0]*11

for e in edges:
    lst[e[0]].append(e[1])

def dfs(node):
    visited[node] = 1
    path[node] = 1
    
    for n in lst[node]:
        if not visited[n]:
            if dfs(n):
                return True
        elif path[n]:
            return True
    
    path[node] = 0
    
    return False
    
for i in range(1, 11):
    if not visited[i]:
        if dfs(i): print(True)

# cycle in undirected graph
import collections

edges = [(1,2),(1,3),(2,5),(5,7),(3,6),(6,7),(3,4)]

lst = collections.defaultdict(list)
visited = [0]*8

for e in edges:
    lst[e[0]].append(e[1])
    lst[e[1]].append(e[0])

def dfs(node, parent):
    visited[node] = 1
    
    for n in lst[node]:
        if not visited[n]:
            if dfs(n, node):
                return True
        elif parent != n:
            # print(node, parent, n)
            return True
    
    return False
    
for i in range(1, 8):
    if not visited[i]: 
        if dfs(i, -1): 
            print(True)

# Directed graph - shortest path
import collections
import heapq

edges = [(0,1,2),(1,2,3),(0,4,1),(4,2,2),(2,3,6),(4,5,4),(5,3,1)]

lst = collections.defaultdict(list)
distance = [float('inf')]*6

for a in edges:
    lst[a[0]].append((a[1], a[2]))
    
l = [(0, 0)]
distance[0] = 0
heapq.heapify(l)

while l:
    d, src = heapq.heappop(l)
    
    for n in lst[src]:
        if distance[n[0]] > distance[src] + n[1]:
            heapq.heappush(l, (distance[src] + n[1], n[0]))
            distance[n[0]] = distance[src] + n[1]
            
print(distance)
# [0, 2, 3, 6, 1, 5]

# Dijkstra (undirected only)
import collections
from collections import deque
import heapq

# edges = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
edges = [[0,1, 1], [0,2, 6], [1,2, 3]]

lst = collections.defaultdict(list)
distance = [float('inf')]*3

for e in edges:
    lst[e[0]].append((e[1],e[2]))
    lst[e[1]].append((e[0],e[2]))

l = [(0,2)]
heapq.heapify(l)


distance[2] = 0

while l:
    d, node = heapq.heappop(l)
    
    for n in lst[node]:
        if d + n[1] < distance[n[0]]:
            distance[n[0]] = d + n[1]
            heapq.heappush(l, (d + n[1], n[0]))
            
print(distance)
# [4,3,0]