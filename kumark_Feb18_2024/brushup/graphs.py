# shortest distance src node
a = [(5,4),(1,2),(2,3),(2,4),(3,5)]
src = 2

import collections

distance = [float('inf')]* 6

d = collections.defaultdict(list)

for k in a:
    d[k[0]].append(k[1])
    d[k[1]].append(k[0])
  
distance[src] = 0

def shortestdistance(node):
    for n in d[node]:
        if distance[node] + 1 < distance[n]:
            distance[n] = distance[node] + 1
            shortestdistance(n)
                
    return distance
    
shortestdistance(src)
    
print(distance)

# bfs traversal

a = [(1,2),(1,3),(2,4),(2,5),(3,6),(3,7),(5,8)]
src = 1

import collections

visited = [0]* 9
res = []

d = collections.defaultdict(list)

for k in a:
    d[k[0]].append(k[1])
    d[k[1]].append(k[0])
  

def dfs(node):
    if visited[node]:
        return
    
    res.append(node)
    visited[node] = 1
    
    for n in d[node]:
        if not visited[n]:
            dfs(n)
                
    return res
    
dfs(src)
    
print(res)