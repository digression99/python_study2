class Solution(object):
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n
        xhash = {}
        yhash = {}
        mxx = 0
        mxy = 0
        idxx = 0
        idxy = 0

        for i in range(len(ops)):
            for j in range(ops[i][0]):
                xhash.setdefault(j, 0)
                xhash[j] += 1
                if xhash[j] > mxx or (xhash[j] == mxx and idxx < j):
                    idxx = j
                    mxx = xhash[j]

            for j in range(ops[i][1]):
                yhash.setdefault(j, 0)
                yhash[j] += 1
                if yhash[j] > mxy or (yhash[j] == mxy and idxy < j):
                    idxy = j
                    mxy = yhash[j]


        return (idxx + 1) * (idxy + 1)

ops = [[2, 2], [3, 3]]
ops2 = [[1, 1]]

print(Solution().maxCount(1, 1, ops2))
#test = {1 : 5, 3 : 3}




