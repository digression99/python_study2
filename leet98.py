# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        if not root:
            return False

        q = []

        q.append(root)

        while q:
            u = q.pop(0)
            if u.left.val > u.val:
                return False
            else:
                q.append(u.left)
            if u.right.val < u.val:
                return False
            else:
                q.append(u.right)
        return True

