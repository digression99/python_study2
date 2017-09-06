# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ans = []
        lev = 0
        q = []
        q.append(root)

        while q:
            ans.append([])
            l = len(q)
            for i in range(l):
                u = q.pop(0)
                if not lev % 2:
                    ans[lev].append(u.val)
                else:
                    ans[lev].insert(0, u.val)
                if u.left:
                    q.append(u.left)
                if u.right:
                    q.append(u.right)
            lev += 1
        return ans

n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

print(Solution().zigzagLevelOrder(n1))






