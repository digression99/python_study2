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
    def addEdge(self, src, dest):
        newNode = AdjListNode(dest)
        newNode.next = self.array[src].head
        self.array[src].head = newNode

        newNode2 = AdjListNode(src)
        newNode2.next = self.array[dest].head
        self.array[dest].head = newNode2
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

v = 5
g = Graph(v)

g.addEdge(0, 1)
g.addEdge(0, 4)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 3)
g.addEdge(3, 4)

g.printGraph()





