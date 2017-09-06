class Solution(object):
    def getRow(self, rowIndex):
        l = [1, 2, 1]

        for _ in range(rowIndex - 1):
            for i in range(1, len(l)):
                t = l[i]
                l[i] = t + l[i - 1]
            l.append(1)
        return l

        """
        :type rowIndex: int
        :rtype: List[int]
        """

print(Solution().getRow(3))