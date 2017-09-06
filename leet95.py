# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addNode(self, root, key):
        if root.val > key:
            if root.left:
                self.addNode(root.left, key)
            else:
                root.left = TreeNode(key)
                return
        if root.val < key:
            if root.right:
                self.addNode(root.right, key)
            else:
                root.right = TreeNode(key)
                return

    def makeTree(self, l):
        root = TreeNode(l[0])
        for i in range(1, len(l)):
            self.addNode(root, l[i])
        return root

    def generateTrees(self, n):
        if n == 0:
            return None
        if n == 1:
            return TreeNode(1)






        """
        :type n: int
        :rtype: List[TreeNode]
        """
