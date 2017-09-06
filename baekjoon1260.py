
class Graph2(object):
    def __init__(self, v):
        self.v = v
        self.array = [[] for i in range(1001)] # adjacency list

    def addEdgeDirected(self, src, dest):
        self.array[src].append(dest)

    def addEdgeUndirected(self, src, dest):
        self.addEdgeDirected(src, dest)
        self.addEdgeDirected(dest, src)

    def bfsstart(self, start):
        visited = [False] * 1001
        self.bfs(visited, start)

    def dfsstart(self, start):
        visited = [False] * 1001
        self.dfs(visited, start)

    def dfs(self, visited, start):
        visited[start] = True
        print(start, end=' ')
        for n in self.array[start]:
            if not visited[n]:
                self.dfs(visited, n)

    def bfs(self, visited, start):
        q = []
        q.append(start)
        visited[start] = True

        while q:
            u = q.pop(0)
            print(u, end=' ')
            for n in self.array[u]:
                if not visited[n]:
                    q.append(n)
                    visited[n] = True

inp = list(map(int, input().split()))
v, m, start = inp[0], inp[1], inp[2]
g = Graph2(1001)

for i in range(m):
    inp = list(map(int, input().split()))
    g.addEdgeUndirected(inp[0], inp[1])

g.dfsstart(start)
print()
g.bfsstart(start)