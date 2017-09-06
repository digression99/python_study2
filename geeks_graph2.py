# graph representation
# adjacency list
class AdjListNode(object):
    def __init__(self, dest):
        self.dest = dest
        self.next = None

class AdjList(object):
    def __init__(self):
        self.head = None

class Graph(object):
    def __init__(self, v):
        self.v = v
        self.array = [AdjList() for i in range(v)]

    def addEdgeUndirected(self, src, dest):
        self.addEdgeDirected(src, dest)
        self.addEdgeDirected(dest, src)

    def addEdgeDirected(self, src, dest):
        newNode = AdjListNode(dest)
        newNode.next = self.array[src].head
        self.array[src].head = newNode

    def printGraph(self):
        for i in range(self.v):
            cur = self.array[i].head
            print("adjacency list of vertex {}\n head".format(i), end='')
            while cur:
                print("-> {}".format(cur.dest), end='')
                cur = cur.next
            print("\n")
    def addVertex(self):
        self.array.append(AdjList())

    def bfs(self, start):
        visited = {}
        for i in range(v):
            visited.setdefault(i, False)
        q = []
        q.append(start)
        visited[start] = True
        while q:
            u = q.pop(0)
            print(u)
            cur = self.array[u].head
            while cur:
                if not visited[cur.dest]:
                    q.append(cur.dest)
                    visited[cur.dest] = True
                cur = cur.next

    def dfs(self, visited, u): # u : now idx number
        print(u)
        #if visited[u] == True:
        #    print(u)
        #    return
        cur = self.array[u].head
        while cur:
            if not visited[cur.dest]:
                visited[cur.dest] = True
                self.dfs(visited, cur.dest)
            cur = cur.next
        #print(u) # dfs without recursion???
    def dfsstart(self, start): # start : node idx number
        visited = [False] * self.v
        visited[start] = True
        self.dfs(visited, start)
from collections import defaultdict



v = 4
g = Graph(v)

g.addEdgeDirected(2, 3)
g.addEdgeDirected(2, 0)
g.addEdgeDirected(0, 2)
g.addEdgeDirected(1, 2)
g.addEdgeDirected(0, 1)
g.addEdgeDirected(3, 3)

#g.bfs(2)
g.dfsstart(2)




