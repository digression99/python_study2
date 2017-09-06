class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

n2.next = n3
n1.next = n2

def printListNode(head):
    t = head
    while t:
        print(t.val)
        t = t.next

def reverseList(head):
    t = head
    dum = ListNode(0)
    dum.next = head
    prev, cur = dum, head
    temp = None
    while prev.next:
        temp = prev
        cur = cur.next
        prev.next.next = temp
        prev = cur
    return head


#printListNode(n1)

reverseList(n1)
printListNode(n1)