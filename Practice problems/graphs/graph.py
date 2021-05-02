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

    for _ in range(N):
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

 ################################ Check for cycle graph ##################################################

def cycle_build_graph(edges, N):
    graph = {}
    visited = [0]*N
    
    for src, dest in edges:
        graph.setdefault(src, []).append(dest)
        graph.setdefault(dest, []).append(src)

    for _ in range(N):
        if visited[0] == 0:
            return cycle_check(graph, 1, visited, -1)
    
def cycle_check(graph, nodes, visited, parent):
    visited[nodes-1] = 1

    for child in graph[nodes]:
        if visited[child-1] == 0:
            if cycle_check(graph, child, visited, nodes):
                return True
        else:
            if child != parent:
                return True
    return False

N = 6
edges = [
        (1, 2),
        (2,3),
        (2,4),
        (3,4),
        (4, 5)
    ]
print(cycle_build_graph(edges, N))  # True

################################ Longest Path in Graph ##################################################

def longest_path_build_graph(edges, N):
    graph = {}
    visited = [0]*N
    
    for src, dest in edges:
        graph.setdefault(src, []).append(dest)
        graph.setdefault(dest, []).append(src)

    for _ in range(N):
        if visited[0] == 0:
            maxdistance, maxnode  = longest_path_dfs(graph, 1, visited, 0, maxD=-1, maxNode=-1)

    # do dfs call with maxnode and find longest path
    visited = [0]*N     # resets visit array for new dfs
    maxdistance, maxnode  = longest_path_dfs(graph, maxnode, visited, 0, maxD=-1, maxNode=-1)
    
    return maxdistance, maxnode
    
def longest_path_dfs(graph, nodes, visited, distance, maxD, maxNode):
    visited[nodes-1] = 1

    if maxD < distance : 
        maxD = distance
        maxNode = nodes

    for child in graph[nodes]:
        if visited[child-1] == 0:
            maxD, maxNode = longest_path_dfs(graph, child, visited, distance + 1, maxD, maxNode)

    return maxD, maxNode

N = 6
edges = [
        (1, 2),
        (2,3),
        (2,4),
        (3,4),
        (4, 5)
    ]
print(longest_path_build_graph(edges, N))  # (3, 1)

################################ Shortest Path in Graph using DFS ##################################################

def shortest_path_build_graph(edges, N):
    graph = {}
    visited = [0]*N
    distance =[0] * N
    
    for src, dest in edges:
        graph.setdefault(src, []).append(dest)
        graph.setdefault(dest, []).append(src)

    for _ in range(N):
        if visited[0] == 0:
            d = shortest_path_dfs(graph, 1, visited, distance, 0)
        
    return d
    
def shortest_path_dfs(graph, nodes, visited, distance,d):
    visited[nodes-1] = 1
    distance[nodes-1] = d

    for child in graph[nodes]:
        if visited[child-1] == 0:
            shortest_path_dfs(graph, child, visited, distance, d + 1)

    return distance

N = 6
edges = [
        (1, 2),
        (2,3),
        (2,4),
        (4, 5),
        (4,6)
    ]
print('shortest path using dfs:', shortest_path_build_graph(edges, N))  # [0, 1, 2, 2, 3, 3]

################################ Shortest Path in Graph using BFS ##################################################

from collections import deque

q = deque()

def bfs_shortest_path_build_graph(edges, N):
    graph = {}
    visited = [0]*N
    distance =[0] * N
    
    for src, dest in edges:
        graph.setdefault(src, []).append(dest)
        graph.setdefault(dest, []).append(src)

    for _ in range(N):
        if visited[0] == 0:
            d = shortest_path_bfs(graph, 1, visited, distance, 0)
        
    return d
    
def shortest_path_bfs(graph, nodes, visited, distance,d):
    visited[nodes-1] = 1
    distance[nodes-1] = d

    q.append(nodes)

    while len(q) > 0:
        el = q.pop()
        for child in graph[el]:
            if visited[child-1] == 0:
                q.append(child)
                distance[child-1] = distance[el-1] + 1

    return distance

N = 6
edges = [
        (1, 2),
        (2,3),
        (2,4),
        (4, 5),
        (4,6)
    ]
print('shortest path using bfs:', shortest_path_build_graph(edges, N)) # [0, 1, 2, 2, 3, 3]

################################ Prime path using BFS ##################################################

"""
find the cheapest prime path between any two given four-digit primes. In one step, only digit can be changed
Input:

A - 1033 
B - 8179  

Output : 
6 steps

    1033
    1733     
    3733     
    3739     
    3779
    8779
    8179    
"""
from collections import deque

primes = []
bfs_graph = {}
visited = [0] * 10000 
distance = [0] * 10000 

q = deque()

def isPrime(n):
    if n == 1: 
        return False

    for i in range(2, n):
        if i**2 <= n:
            if n % i == 0:
                return False

    return True 

def isValid(a, b):
    cnt = 0
    while a > 0:
        if ((a % 10) != (b % 10)):
            cnt += 1
        a = a//10
        b = b//10
    
    if cnt == 1: 
        return True
    else:
        return False

def prime_path_bfs(bfs_graph, src):
    q.append(src)
    visited[src] = 1
    distance[src] = 0

    while len(q) > 0:
        elm = q.popleft()       # changed to popleft 

        for child in bfs_graph[elm]:
            if not(visited[child]):
                visited[child] = 1
                q.append(child)
                distance[child] = distance[elm] + 1

    return distance

def prime_path_build_graph(src,trgt):
    for i in range(src, trgt+1):
        if isPrime(i):
            primes.append(i)

    for i in range(len(primes)-1):
        for j in range(i +1 , len(primes)):
            if isValid(primes[i], primes[j]):
                bfs_graph.setdefault(primes[i], []).append(primes[j])
                bfs_graph.setdefault(primes[j], []).append(primes[i])

    return prime_path_bfs(bfs_graph, src)[trgt]

print(prime_path_build_graph(1033, 8179))       # 6

################################ Social Networking Distance using BFS ##################################################
from collections import deque

q = deque()

def social_network_build_graph(edges, N, src_input, lvl):
    social_network_graph = {}

    for src, dest in edges:
        social_network_graph.setdefault(src,[]).append(dest)
        social_network_graph.setdefault(dest,[]).append(src)

    return social_network_bfs(social_network_graph, N, src_input, lvl)

def social_network_bfs(social_graph, N, src, lvl):
    visited = [0] * (N+1)
    level = [0] * (N+1)
    distance = [0] * (N+1)

    q.append(src)
    visited[src] = 1
    distance[src] = 0

    while len(q) > 0:
        el = q.pop()
        for child in social_graph[el]:
            if not(visited[child]):
                visited[child] = 1
                distance[child] = distance[el] + 1
                q.append(child)
                level[distance[child]] += 1 

    return level[lvl]

N = 9
edges = [
        (1, 2),
        (7, 1),
        (2, 3),
        (2, 4),
        (3, 4),
        (6, 7),
        (9, 7),
        (4, 7),
        (7, 8),
        (5, 6)
    ]

print(social_network_build_graph(edges, N, 7, 1))   # 5 nodes which are 1 level away from src_node
print(social_network_build_graph(edges, N, 5, 2))   # 1 node  which are 2 levels away from src_node

################################ 2D Grid using DFS ##################################################

def grid_2d_dfs_isValid(x, y, M, N, grid_2d_dfs_visited):
    if x < 1 or y < 1 or x > M or y > N:
        return False
    
    if grid_2d_dfs_visited[x][y]:
       return False

    return True

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

def dfs_traversal(x, y, M, N, grid_2d_dfs_visited):
    grid_2d_dfs_visited[x][y] = 1

    print(str(x) + ' ' + str(y))

    if grid_2d_dfs_isValid(x-1, y, M, N, grid_2d_dfs_visited):
        dfs_traversal(x-1,y, M, N, grid_2d_dfs_visited)
    if grid_2d_dfs_isValid(x, y+1, M, N, grid_2d_dfs_visited):
        dfs_traversal(x,y+1, M, N, grid_2d_dfs_visited)
    if grid_2d_dfs_isValid(x+1, y, M, N, grid_2d_dfs_visited):
        dfs_traversal(x+1,y, M, N, grid_2d_dfs_visited)
    if grid_2d_dfs_isValid(x, y-1, M, N, grid_2d_dfs_visited):
        dfs_traversal(x,y-1, M, N, grid_2d_dfs_visited)

    # alternate way to use above approach
    # for i in range(4):
    #     if grid_2d_dfs_isValid(x+dx[i], y+dy[i],  M, N, grid_2d_dfs_visited):
    #         dfs_traversal(x+dx[i], y+dy[i],  M, N, grid_2d_dfs_visited)

N= 3
M= 3
grid_2d_dfs_visited = [[0 for _ in range(N+1)] for _ in range(M+1)]
print('dfs path traversal on 2d grid..')
dfs_traversal(1,1, 3, 3, grid_2d_dfs_visited)

################################ Connected component in 2D Grid using DFS ##################################################

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def connected_component_2d_isvalid(x, y, arr, dfs_visited):
    if x < 0 or y < 0 or x > len(arr) -1 or y > len(arr[0]) -1:
        return False
    
    if dfs_visited[x][y] or arr[x][y] == 0:
        return False
    return True

def connected_component_2d_dfs_traversal(x, y, arr, dfs_visited):
    dfs_visited[x][y] = 1

    for i in range(4):
        if connected_component_2d_isvalid(x+dx[i], y+dy[i], arr, dfs_visited):
            connected_component_2d_dfs_traversal(x+dx[i], y+dy[i], arr, dfs_visited)

def connected_component_2d(x, y, arr, dfs_visited):
    grid_connected_component_count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1 and not(dfs_visited[i][j]):
                grid_connected_component_count += 1
                connected_component_2d_dfs_traversal(i, j, arr, dfs_visited)

    return grid_connected_component_count


arr = [
    [0, 0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1],
]
grid_2d_dfs_visited = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
print('connected components in dfs path traversal on 2d grid..')
print(connected_component_2d(0, 0, arr,grid_2d_dfs_visited))    # 6

################################ 2D Grid using BFS ##################################################

from collections import deque

q = deque()

def grid_2d_bfs_isValid(x, y, M, N, grid_2d_bfs_visited):
    if x < 0 or y < 0 or x > M-1 or y > N-1:
        return False
    
    if grid_2d_bfs_visited[x][y]:
       return False

    return True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs_traversal(x, y, M, N, grid_2d_bfs_visited,grid_2d_bfs_distance):
    q.append((x, y))
    grid_2d_bfs_visited[x][y] = 1

    while len(q) > 0:
        el = q.popleft()
        x, y = el[0], el[1]
        for i in range(4):
            newx, newy = x+dx[i], y+dy[i]
            if grid_2d_bfs_isValid(newx, newy,  M, N, grid_2d_bfs_visited):
                grid_2d_bfs_visited[newx][newy] = 1
                grid_2d_bfs_distance[newx][newy] = grid_2d_bfs_distance[x][y] + 1
                q.append((newx, newy))
    
    for i in range(M):
        for j in range(N):
            print(grid_2d_bfs_distance[i][j], end=" ")
        print(sep="\n")

N= 4
M= 4
grid_2d_bfs_visited = [[0 for _ in range(N)] for _ in range(M)]
grid_2d_bfs_distance = [[0 for _ in range(N)] for _ in range(M)]
print('bfs path traversal on 2d grid..')
bfs_traversal(0,0, M, N, grid_2d_bfs_visited, grid_2d_bfs_distance)
"""
0 1 2 3
1 2 3 4
2 3 4 5
3 4 5 6
"""

################################ Number of Islands using BFS ##################################################
from collections import deque

q = deque()

"""
matrix has below co-ordinates:
-1, 0  - prev row same col
-1, -1 - prev row prev col
0, -1  - same row prev col
0, 1   - same row next col
-1, 1  - prev row next col
1, -1  - next row prev col
1, 0   - next row same col
1, 1   - next row same col
"""

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [0, 1, -1, -1, 1, 0, 1, -1]

def islands_is_valid(x, y, arr, grid_2d_num_of_islands_visited):
    if x < 0 or y < 0 or x > len(arr) - 1 or y > len(arr[0]) - 1:
        return False
    
    if arr[x][y] == 0 or grid_2d_num_of_islands_visited[x][y]:
        return False
    
    return True

def bfs_num_of_islands_traversal(x, y, arr, grid_2d_num_of_islands_visited):
    q.append((x,y))
    grid_2d_num_of_islands_visited[x][y] = 1

    while len(q) > 0:
        el = q.popleft()
        X, Y = el[0], el[1]
        for i in range(8):
            newX, newY = X +dx[i], Y+dy[i]
            if islands_is_valid(newX, newY, arr, grid_2d_num_of_islands_visited):
                grid_2d_num_of_islands_visited[newX][newY] = 1
                q.append((newX, newY))

def number_of_islands(arr, grid_2d_num_of_islands_visited):
    number_of_islands = 0 
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1 and not(grid_2d_num_of_islands_visited[i][j]):
                bfs_num_of_islands_traversal(i, j, arr, grid_2d_num_of_islands_visited)
                number_of_islands += 1

    return number_of_islands

arr = [
 [ 1, 1, 0, 0, 0 ],
 [ 0, 1, 0, 0, 1 ],
 [ 1, 0, 0, 1, 1 ],
 [ 0, 0, 0, 0, 0 ],
 [ 1, 0, 1, 0, 1 ]
]

grid_2d_num_of_islands_visited = [[0 for i in range(len(arr[0]))] for i in range(len(arr))]
print('number of islands using BFS..')
print(number_of_islands(arr, grid_2d_num_of_islands_visited))   # 5 

################################ Knight moves using BFS ##################################################

from collections import deque

knight_q = deque()

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def knight_valid_position(x, y, N, M, knight_moves_bfs_visited):
    if x < 0 or y < 0 or x > N  or y > M :
        return False

    if knight_moves_bfs_visited[x][y]:
        return False
    
    return True

def knight_moves_bfs_traversal(N, M, src, tgt, knight_moves_bfs_visited, knight_moves_bfs_distance):
    knight_q.append(src)
    knight_moves_bfs_visited[src[0]][src[1]] = 1

    while len(knight_q) > 0:
        el = knight_q.popleft()
        x, y = el[0], el[1]

        if x == tgt[0] and y == tgt[1]:
            return knight_moves_bfs_distance[x][y]

        for i in range(8):
            newx, newy = x+dx[i], y+dy[i]
            if knight_valid_position(newx, newy, N, M, knight_moves_bfs_visited):
                knight_moves_bfs_visited[newx][newy] = 1
                knight_moves_bfs_distance[newx][newy] = knight_moves_bfs_distance[x][y] + 1
                knight_q.append((newx, newy))

                if newx == tgt[0] and newy == tgt[1]:
                    return knight_moves_bfs_distance[newx][newy]

N = 8
M = 8
knight_moves_bfs_visited = [[0 for _ in range(N+1)] for _ in range(M+1)]
knight_moves_bfs_distance = [[0 for _ in range(N+1)] for _ in range(M+1)]
src= (1, 1)
target = (2,1)
print('knight moves using bfs..')
print(knight_moves_bfs_traversal(N, M, src, target, knight_moves_bfs_visited, knight_moves_bfs_distance))   # 3