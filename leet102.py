# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, root, l, lev):
        if not root:
            return

        if lev > len(l) - 1:
            l.append([])
        l[lev].append(root.val)
        self.dfs(root.left, l, lev + 1)
        self.dfs(root.right, l, lev + 1)

    def levelOrder(self, root):
        if not root:
            return [[]]
        l = [[]]
        self.dfs(root, l, 0)

        return l

n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

print(Solution().levelOrder(n1))