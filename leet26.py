class Solution(object):
    def removeDuplicates(self, nums):
        i = 0

        while i < len(nums):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    del nums[i + 1]
            i += 1
        return len(nums)

obj = Solution()
l = [1, 1]

print(obj.removeDuplicates(l))