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