class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        if not head:
            return head
        if n == m:
            return head

        dum = ListNode(0)
        dum.next = head
        revstart, revend = None, None
        cur, nxt = dum, head
        start, end = None, None

        for _ in range(m - 1):
            cur = nxt
            nxt = nxt.next
        start = cur

        for _ in range(n - m + 1):
            cur = nxt
            if nxt:
                nxt = nxt.next
            if revend == None:
                revend = cur
                cur.next = None
            else:
                cur.next = revstart
            revstart = cur

        revend.next = nxt
        start.next = revstart

        return dum.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n5.next = None
n4.next = n5
n3.next = n4
n2.next = n3
n1.next = n2
#Solution().reverseBetween(n1, 2, 4)

nn1 = ListNode(3)
nn2 = ListNode(5)
nn2.next = None
nn1.next = nn2

Solution().reverseBetween(nn1, 1, 2)



