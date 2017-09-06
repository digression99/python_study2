class Solution(object):
    def dp(self, nums, d, idx, n):
        if idx >= n:
            d[idx] = 1
            return True

        if d[idx] > 0:
            return True if d[idx] == 1 else False

        for i in range(nums[idx], 0, -1):
            if idx + i >= n or self.dp(nums, d, idx + i, n):
                return True
        d[idx] = 2
        return False

    def canJump(self, nums):
        d = [0] * (len(nums) + 2)
        return self.dp(nums, d, 0, len(nums) - 1)

obj = Solution()
print(obj.canJump([2, 3, 1, 1, 4]))
#print(obj.canJump([3, 2, 1, 0, 4]))
#print(obj.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,
#                   2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4,
#                   3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7]))