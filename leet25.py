class ListNode(object):
    def __init(self, data):
        self.data = data
        self.next = None

class Solution(object):

    def getLen(self, head):
        t = head
        rep = 1
        while t.next:
            t = t.next
            rep += 1
        return rep

    def reverseKGroup(self, head, k):
        if head == None or head.next == None:
            return head

        d = ListNode(0) # dummy

        #for manipulation
        prev = d
        nxt = head.next
        cur = head

        #for connection
        start = head
        tail = head
        tgt = head

        rep = self.getLen(head) // k

        for i in range(0, rep):
            prev = d
            start = cur
            end = cur

            #get the end
            for u in range(0, k - 1):
                end = end.next
            tgt = end.next # node to link later

            for j in range(0, k):
                cur.next = prev
                prev = cur
                cur = nxt
                if nxt.next:
                    nxt = nxt.next
            # at the end.

            # connect the cutted list
            tail.next = prev
            start.next = tgt
            tail = start

            if i == 0:
                head = prev
            if tgt:
                start.next = tgt
            else:
                start.next = None

        return head