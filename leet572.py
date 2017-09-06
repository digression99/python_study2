# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def check(self, sNode, tNode):
        if sNode.val != tNode.val:
            return False
        if not sNode.left and tNode.left or sNode.left and not tNode.left:
            return False
        if not sNode.right and tNode.right or sNode.right and not tNode.right:
            return False
        b1 = True
        b2 = True
        if sNode.left and tNode.left:
            b1 = self.check(sNode.left, tNode.left)
        if sNode.right and tNode.right:
            b2 = self.check(sNode.right, tNode.right)
        return b1 and b2

    def search(self, sNode, tNode):
        if sNode.val == tNode.val:
            return sNode
        l = self.search(sNode.left, tNode)
        if l.val == tNode.val:
            return l
        r = self.search(sNode.right, tNode)
        if r.val == tNode.val:
            return r

    def isSubtree(self, s, t):
        if not s: return False
        if self.check(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

        # while s:
        #     root = s
        #     l = s.left
        #     r = s.right
        #     if
        #
        #     root = self.search(s, t)
        #     if self.check(root, t):
        #         return True


n1 = TreeNode(object)
n1.val = 3
n2 = TreeNode(object)
n2.val = 4
n3 = TreeNode(object)
n3.val = 5
n4 = TreeNode(object)
n4.val = 1
n5 = TreeNode(object)
n5.val = 2
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

n6 = TreeNode(object)
n6.val = 4
n7 = TreeNode(object)
n7.val = 1
n8 = TreeNode(object)
n8.val = 2

n6.left = n7
n6.right = n8


print(Solution().isSubtree(n1, n6))


