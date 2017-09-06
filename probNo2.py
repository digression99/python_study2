# Definition for singly-linked list.
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

class ListNode(object):
    def __init__(self, x):
        newNode = Node(x)
        newNode.setNext(self.next)
        self.next = newNode
        self.size = 1

    def insert(self, val):
        newNode = Node(val)
        newNode.setNext(self.next)
        self.next = newNode
        self.size += 1

    def getSize(self):
        return self.size

    def search(self, data):
        cur = self.next
        found = False
        while cur and found is False:  # till cur is not None
            if cur.getData() == data:
                found = True
            else:
                cur = cur.getNext()
        if cur is None:
            return -1  # raise ValueError("data not in list")
        return cur

    def delete(self, data):
        cur = self.next
        prev = None
        found = False

        while cur and found is False:
            if cur.getData() == data:
                found = True
            else:
                prev = cur
                cur = cur.getNext()

        if cur is None:
            return -1  # raise ValueError("data not in list")
        if prev is None:
            self.next = cur.getNext()  # 사이즈가 1이라면 자동으로 None이 된다??
        else:
            prev.setNext(cur.getNext())
        self.size -= 1


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        cur1 = l1.next  # i
        cur2 = l2.next  # j
        dat1 = cur1.getData()
        dat2 = cur2.getData()
        sum = dat1 + dat2 + c
        c = int(sum / 10)
        newList = ListNode(sum % 10)

        while True:
            if cur1 is None:
                dat1 = 0
            else:
                dat1 = cur1.getData()
                cur1 = cur1.getNext()

            if cur2 is None:
                dat2 = 0
            else:
                dat2 = cur2.getData()
                cur2 = cur2.getNext()

            sum = dat1 + dat2 + c
            c = int(sum / 10)
            newList.insert(sum % 10)

            if cur1 is None and cur2 is None:
                break

        return newList
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
