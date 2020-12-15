
class arrivalDepartureDFS(object):
    def __init__(self, n, edges):
        self.arrival = [0] * n
        self.departure = [0] * n
        self.graph = [[] for _ in range(n)]
        self.visited = [False] * n
        for (src, dest) in edges:
            self.graph[src].append(dest)
    
    
    def DFS(self, node, time):
        time += 1
        self.arrival[node] = time
        self.visited[node] = True
        for i in range(len(self.graph)):
            if not(self.visited[i]):
                time = self.DFS(i, time)
        time += 1
        self.departure[node] = time
        return time
    

    def printDFS(self,n):
        for i in range(n):
            print("Vertices:" + str(i) + "(" + str(self.arrival[i]) + "," + str(self.departure[i]) + ")")

N = 8
edges = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 1), (3, 5), (4, 5), (6, 7)]
dfs = arrivalDepartureDFS(N, edges)
dfs.DFS(0, -1)
dfs.printDFS(N)