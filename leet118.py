class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        l = [[1]]
        for i in range(numRows - 1):
            row = [1]
            for j in range(len(l[i]) - 1):
                row.append(l[i][j] + l[i][j + 1])
            row.append(1)
            l.append(row)
        return l

        """
        :type numRows: int
        :rtype: List[List[int]]
        """

print(Solution().generate(5))
