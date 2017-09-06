# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        #
        # traverse the linkedlist, if you find the node value less than x,
        # move the node before the node greater than or equal to x.
        # keep the end node of the min part. next is the start of max part.
        # if you find the node value greater than or equal to x,
        # just skip it.
        dum = ListNode(-1)
        dum.next = head
        lend = ListNode(-1)
        lend.next = None
        prev, cur, nxt, lstart = dum, head, head.next, lend

        while cur:
            if cur.val < x:
                # make a new node? or just change the prev and cur to change the
                cur.next = None
                lend.next = cur

                prev.next = nxt
                lend = lend.next
            else:
                prev = cur
            cur = nxt
            if cur:
                nxt = nxt.next

        lend.next = dum.next
        return lstart.next

#1->4->3->2->5->2 and x = 3

n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(5)
n6 = ListNode(2)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

head = Solution().partition(n1, 3)
while head:
    print(head.val)
    head = head.next



