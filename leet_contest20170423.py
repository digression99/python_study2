class Solution(object):
    def __init__(self):
        self.offset = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [1, 1], [1, -1], [-1, 1]]

    def checkMax(self, M, D, i, j, rs, cs):
        mx = 1
        for k in range(0, 8, 2):
            newi = i + self.offset[k][0]
            newj = j + self.offset[k][1]
            nowmax = 1
            leftendi = i
            leftendj = j
            rightendi = i
            rightendj = j

            while 0 <= newi < cs and 0 <= newj < rs and M[newi][newj]:
                nowmax += 1
                newi += self.offset[k][0]
                newj += self.offset[k][1]
            leftendi = newi - self.offset[k][0]
            leftendj = newj - self.offset[k][1]

            newi = i + self.offset[k + 1][0]
            newj = j + self.offset[k + 1][1]

            while 0 <= newi < cs and 0 <= newj < rs and M[newi][newj]:
                nowmax += 1
                newi += self.offset[k + 1][0]
                newj += self.offset[k + 1][1]
            rightendi = newi - self.offset[k + 1][0]
            rightendj = newj - self.offset[k + 1][1]

            if mx < nowmax:
                mx = nowmax
                for u in range(leftendi, rightendi + 1):
                    for v in range(leftendj, rightendj + 1):
                        D[u][v] = mx
            mx = max(mx, nowmax)
        D[i][j] = mx
        return mx

    def longestLine(self, M):
        if not M:
            return 0
        rowSize, colSize = len(M[0]), len(M)
        D = [[0] * rowSize for i in range(colSize)]
        mx = 0

        for i in range(colSize):
            for j in range(rowSize):
                if M[i][j] == 1 :
                    if (mx > 0 and D[i][j] < mx) or mx == 0:
                        mx = max(mx, self.checkMax(M, D, i, j, rowSize, colSize))
        return mx

l = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
l2 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
l3 = [[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]]
obj = Solution()

print(obj.longestLine(l3))