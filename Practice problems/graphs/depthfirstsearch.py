# below method will implement DFS graph using python
import abc
from collections import deque, defaultdict

class Edge(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def addEdge(self, src, dest):
        pass

class Graph(Edge):
    def __init__(self, numofnodes):
        self.numofnodes = numofnodes
        self.graph= {}

    def addEdge(self, src, dest):
        return self.graph.setdefault(src, []).append(dest)


class DFS(Graph):
    
    def __init__(self, numofnodes, startnode=0):
        super().__init__(numofnodes)        
        self.startnode = startnode
        self.queue = deque()
        self.queue.append(self.startnode)
        self.result = [[]]
        
    def visited_array(self):
        self.visited = [False for _ in range(self.numofnodes)]
        return self.visited

    def executeDFS(self, vertex):
        array = self.visited_array()
        array[vertex] = True
        while self.queue:
            curlist = []
            for _ in range(len(self.queue)):
                curval = self.queue.pop()
                curlist.append(curval)
                for i in range(len(self.graph[curval])):
                    print(self.graph[curval], type(i))
                    if not(array[self.graph[curval][i]]):
                        self.queue.append(self.graph[curval][i])
            
            self.result.append(curlist)

        return self.result[1:]
                


g = DFS(4, 2)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,2)
print(g.executeDFS(2))