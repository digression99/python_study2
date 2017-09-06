class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        ht = {}
        totNum = 0
        i = 0
        leng = len(nums)
        while i < leng:
            ht.setdefault(nums[i], 0)
            if ht[nums[i]] >= 2:
                while i < leng and nums[i - 1] == nums[i]:
                    nums.pop(i)
                    leng -= 1
            else:
                ht[nums[i]] += 1
                totNum += 1
                i += 1
        return totNum

l = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(l))