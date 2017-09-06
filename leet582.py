class Node():
    def __init__(self, val=-1):
        self.val = val
        self.childlist = []
        #self.left = None
        #self.right = None

class Solution(object):
    def searchNode(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        for c in root.childlist:
            nd = self.searchNode(c, val)
            if nd:
                return nd
        return None



        #t1 = self.searchNode(root.left, val)
        #t2 = self.searchNode(root.right, val)
        # assume that definitely there's a root
        #if t1:
        #    return t1
        #else:
        #    return t2

    def makeTree(self, root, pid, ppid):
        if not root:
            return None
        while pid:
            if root.val in ppid:
                while root.val in ppid:
                    i = ppid.index(root.val)
                    nd = self.searchNode(root, root.val)
                    nd.childlist.append(Node(pid[i]))
                    # if not nd.left:
                    #     nd.left = Node(pid[i])
                    # else:
                    #     nd.right = Node(pid[i])
                    pid.pop(i)
                    ppid.pop(i)
            else:
                for c in root.childlist:
                    self.makeTree(c, pid, ppid)
                #self.makeTree(root.left, pid, ppid)
                #self.makeTree(root.right, pid, ppid)
                break

        # for i in range(len(pid)):
        #     nd = self.searchNode(root, ppid[i])
        #     if not nd.left:
        #         nd.left = Node(pid[i])
        #     else:
        #         nd.right = Node(pid[i])
        # return root

    def killNode(self, root, l):
        if not root:
            return
        if root:
            l.append(root.val)

        for c in root.childlist:
            self.killNode(c, l)

        #self.killNode(root.left, l)
        #self.killNode(root.right, l)


    def killProcess(self, pid, ppid, kill):
        l = []
        root = Node()
        for i in range(len(ppid)):
            if ppid[i] == 0:
                root.val = pid[i]
                ppid.pop(i)
                pid.pop(i)
                break

        self.makeTree(root, pid, ppid)
        nd = self.searchNode(root, kill)
        self.killNode(nd, l)
        return l

pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5

print(Solution().killProcess(pid, ppid, kill))