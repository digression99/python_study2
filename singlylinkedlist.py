class Node(object):
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNext(self, newNext):
        self.nextNode = newNext

class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode
        self.size += 1

    def getSize(self):
        return self.size

    def search(self, data):
        cur = self.head
        found = False
        while cur and found is False: # till cur is not None
            if cur.getData() == data:
                found = True
            else:
                cur = cur.getNext()
        if cur is None:
            return -1   # raise ValueError("data not in list")
        return cur

    def delete(self, data):
        cur = self.head
        prev = None
        found = False

        while cur and found is False:
            if cur.getData() == data:
                found = True
            else:
                prev = cur
                cur = cur.getNext()

        if cur is None:
            return -1 # raise ValueError("data not in list")
        if prev is None:
            self.head = cur.getNext() # 사이즈가 1이라면 자동으로 None이 된다??
        else:
            prev.setNext(cur.getNext())
        self.size -= 1

    def printAll(self):
        cur = self.head
        while cur:
            print(cur.getData())
            cur = cur.getNext()

    def findEnd(self):
        cur = self.head

        for i in range(0, self.size - 1):
            cur = cur.getNext()

        return cur



