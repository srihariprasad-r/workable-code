# below method will implement BFS graph using python
import abc
from collections import deque

class Edge(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def addEdge(self, src, dest):
        pass

class Graph(Edge):
    def __init__(self, numofnodes):
        self.numofnodes = numofnodes
        self.graph = {}

    def addEdge(self, src, dest):
        if src in self.graph.keys():
            self.graph[src].append(dest)
        else:
            self.graph[src] = [dest]
        return self.graph

class BFS(Graph):
    
    def __init__(self, numofnodes, startnode):
        super().__init__(numofnodes)        
        self.startnode = startnode
        self.queue = deque()
        self.queue.append(self.startnode)
        self.result = [[]]
        
    def visited_array(self):
        self.visited = [False for _ in range(self.numofnodes)]
        return self.visited

    def executeBFS(self):
        array = self.visited_array()
        while self.queue:
            curlist = []
            for _ in range(len(self.queue)):
                node = self.queue.popleft()
                curlist.append(node)
                array[node] = True
                if node in self.graph:                    
                    for i in range(len(self.graph[node])):                        
                        if not(array[self.graph[node][i]]):
                            self.queue.append(self.graph[node][i])

            self.result.append(curlist)

        return self.result[1:]                         


g = BFS(4, 2)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,2)
print(g.executeBFS())

#=====================================================================================================#
# Print all paths from source to destination in undirected graph

from collections import deque
q = deque()

def build_graph(edges, N):
    adj_list = {}
    visited = [0] * N
    
    for src, dest in edges:
        adj_list.setdefault(src, []).append(dest)
        
    return bfs(adj_list, 0, visited, 5)
    
def bfs(adj_list, src, visited, tgt, res =[]):
    q.appendleft([src])
    
    while len(q) > 0:
        el = q.pop()
 
        lst = el[-1]

        if lst == tgt:
            res.append(el)  # when dest is reached, append it to result as path is found
            
        child = adj_list[lst]
            
        for c in child:
            if not visited[c]:
                q.appendleft(el + [c])      # new path is discovered
            
        visited[lst] = 1
            
    return res

N = 6
edges = [
    (0, 1),
    (0, 3),
    (1, 0),
    (1, 2),
    (2, 1),
    (2, 4),
    (3, 0),
    (3, 4),
    (4, 2),
    (4, 3),
    (4, 5),
    (5, 4)
]
print(build_graph(edges, N))  # [[0, 3, 4, 5], [0, 1, 2, 4, 5]]
    
