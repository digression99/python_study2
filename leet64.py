class Solution(object):
    def backtrack(self, grid, x, y, sum):
        if x >= len(grid[0]) or y >= len(grid):
            return sum
        sum += grid[y][x]

        s1 = self.backtrack(grid, x + 1, y, sum)
        s2 = self.backtrack(grid, x, y + 1, sum)

        #if x + 1 == len(grid[0]) - 1 and y == len(grid) - 1:
        #    return s1
        #if x == len(grid[0]) - 1 and y + 1 == len(grid) - 1:
        #    return s2
        if s1 < s2:
            return s1
        return s2

    def minPathSum(self, grid):
        if not grid:
            return 0

        s = 0
        s = self.backtrack(grid, 0, 0, s)

        return s + grid[len(grid) - 1][len(grid[0]) - 1]

map = [[1, 2, 3, 4], [4, 3, 2, 1], [5, 4, 3, 2]]
obj = Solution()
print(obj.minPathSum(map))