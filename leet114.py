# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traverse(self, root, rightp):
        if root.left:
            if root.right:
                self.traverse(root.left, root.right)
            else:
                self.traverse(root.left, rightp)

        t = root.right
        if root.left:
            root.right = root.left
            root.left = None

        if t:
            self.traverse(t, rightp)
        else:
            if not root.right and rightp:
                root.right = rightp

            #t.right = rightp
            #root.right = rightp


    def flatten(self, root):
        if not root:
            return
        # pre order : left -> root -> right
        if root.left:
            self.traverse(root.left, root.right)

        t = root.right
        if root.left:
            root.right = root.left
            root.left = None

        if t:
            self.traverse(t, None)

        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
#
# n1.left = n2
# n1.right = n5
#
# n2.left = n3
# n2.right = n4
#
# n5.right = n6
#
# nn1 = TreeNode(1)
# nn2 = TreeNode(2)
# nn3 = TreeNode(3)
#
# nn1.left = nn2
# nn1.right = nn3

#Solution().flatten(nn1)

#[1,2,null,3,4,5]

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n2.left = n3
n2.right = n4
n3.left = n5

Solution().flatten(n1)






