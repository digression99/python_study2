class Solution(object):
    def numTrees(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        d = [0] * (n + 1)#[[0] for i in range(n + 1)]
        d[0] = 1
        d[1] = 1
        for i in range(2, n + 1):
            totNum = 0
            for j in range(1, i + 1):
                totNum += d[j - 1] * d[i - j]
            d[i] = totNum
        return d[n]








        # for i in range(1, n + 1):
        #     d[i] = self.perm(i)
        #
        # totNum = 0
        # for i in range(1, n + 1):
        #     totNum += d[i - 1] * d[n - i]
        # return totNum

print(Solution().numTrees(4))