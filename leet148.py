class Solution(object):
    def binSort2(self, npos, nl):
        if nl == 0:
            return

        nxtpos = npos
        for i in range(0, nl):
            if nxtpos.next:
                if nxtpos.val > nxtpos.next.val:
                    nxtpos.val, nxtpos.next.val = nxtpos.next.val, nxtpos.val
                nxtpos = nxtpos.next

        nxtpos = npos
        for i in range(0, int(nl / 2)):
            nxtpos = nxtpos.next

        self.binSort2(npos, int(nl / 2))
        self.binSort2(nxtpos, int(nl / 2))

    def sortList(self, head):
        if head == None or head.next == None:
            return head

        count = 0
        it = head
        while it != None:
            count += 1
            it = it.next
        #self.binSort(head, count)
        self.binSort2(head, count)

        return head

class ListNode():
    def __init__(self, val):
