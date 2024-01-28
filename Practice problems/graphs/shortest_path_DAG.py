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
# without PQ:
import collections
from collections import deque

edges = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]

lst = collections.defaultdict(list)
distance = [float('inf')]*6

q = deque()

for e in edges:
    lst[e[0]].append((e[1],e[2]))
    
q.append(0)
distance[0] = 0

while q:
    node = q.popleft()
    
    for n in lst[node]:
        if distance[node] + n[1] < distance[n[0]]:
            distance[n[0]] = distance[node] + n[1]
            q.append(n[0])
            
print(distance)
# [0, 2, 3, 6, 1, 5] 

# with PQ
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

# path with minimum effort
# issue
import collections
from collections import deque

arr = [
    [1,2,2],
    [3,8,2],
    [5,3,5]
]

directions = [(0, -1), (0, 1), (-1,0),(1,0)]
mx = float('inf')
visited = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]

q = deque()
q.append((0, (0, 0)))
visited[0][0] = 1

while q:
    d, a = q.popleft()
    
    if a[0] == len(arr)-1 and a[1] == len(arr[0])-1:
        mx = min(mx, d)
    
    for d in directions:
        newx = a[0] + d[0]
        newy = a[1] + d[1]
        if newx > -1 and newx < len(arr) \
            and newy > -1 and newy < len(arr[0]) \
            and visited[newx][newy] == 0:
                q.append((abs(arr[a[0]][a[1]]- arr[newx][newy]), (newx, newy)))
                visited[newx][newy] = 1
                
print(mx)
# 3

# shortest distance - maze
from collections import deque

grid = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1]
]
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

mx = float('inf')

s = (0,1)
dt = (1,1)

q = deque()
q.append((s, 0))
visited[s[0]][s[1]] = 1

while q:
    a, ds = q.popleft()
    
    if a[0] == dt[0] and a[1] == dt[1] and grid[d[0]][d[1]] == 1:
        mx = min(mx, ds+1)
    
    for d in directions:
        newx = a[0] + d[0]
        newy = a[1] + d[1]
        if newx > -1 and newx < len(grid) and newy > -1 and newy < len(grid[0]):
            if visited[newx][newy] == 0:
                if grid[newx][newy] == 1:
                    q.append(((newx, newy), ds + 1))
                    visited[newx][newy] = 1
                    
print(mx)
# 2