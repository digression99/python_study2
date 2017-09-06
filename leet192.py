# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None





class Solution(object):

    def binSort(self, npos, lenl):
        nl = int(lenl / 2)
        if nl == 1:
            # should check if next exists
            if npos.next.val and (nops.val > npos.next.val):
                npos.val, npos.next.val = npos.next.val, npos.val
                return npos
        nxtpos = npos
        for i in range(0, nl):
            nxtpos = nxtpos.next

        nxtptr = self.binSort(nxtpos, nl)
        nptr = self.binSort(npos, nl)

        # merge process
        l = []
        for i in range(0, lenl):
            if nxtptr.val < nptr:
                l.append(nxtptr.val)

    def sortList(self, head):
        if head.next == None:
            return head

        count = 0
        it = head
        while it.next != None:
            count += 1
            it = it.next

        return self.binSort(head, count)

        """
        :type head: ListNode
        :rtype: ListNode
        """