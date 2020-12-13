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



