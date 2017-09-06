class Solution(object):
    def permuteUnique(self, nums):
        ans = [[]]
        for i in range(len(nums)):
            newlist = []
            for j in range(len(ans)):
                for k in range(len(ans[j]) + 1):
                    new_per = ans[j][:k] + [nums[i]] + ans[j][k:]
                    newlist.append(new_per)
                    if k < len(ans[j]) and nums[i] == ans[j][k]: break
            ans = newlist
                # for k in range(len(ans[i][j]) + 1):
                #     ans[i + 1].append(j[:k] + nums[i] + j[k:])
                    #if nums[i] == j[k]: break
        return ans

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

print(Solution().permuteUnique([1, 1, 2, 2]))