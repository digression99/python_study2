# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, s, t):
        s.append(str(t.val))

        if t.left or t.right:
            s.append("(")
            if t.left:
                self.dfs(s, t.left)
            s.append(")")
            if t.right:
                s.append("(")
                self.dfs(s, t.right)
                s.append(")")

    def tree2str(self, t):
        s = []
        self.dfs(s, t)
        return ''.join(s)



        """
        :type t: TreeNode
        :rtype: str
        """

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)

n1.left = n2
n1.right = n3
n3.left = n4

print(Solution().tree2str(n1))