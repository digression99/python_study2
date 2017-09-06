class Solution():
    def generateMatrix(self, n):
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [list(range(lo, hi))] + list(map(list, zip(*A[::-1])))
            #A = list(range(lo, hi)) + list(zip(*A[::-1]))
        return A


#l = [1, 2, 3, 4, 5, 6]
#l = [[1, 2], [3, 4], [5, 6]]
#l = [[1, 2, 3, 4, 5, 6], [7, 6, 5, 4, 3, 2]]
#l2 = [(1, 2, 3), (4, 5, 6)]
#print(list(zip(*l)))

print(Solution().generateMatrix(3))
#print(list(range(4)))