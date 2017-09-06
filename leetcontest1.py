class Solution(object):
    def dp(self, nums, sp, n):
        if n == 1:
            return nums[n]
        mx = 0
        mn = 0
        for i in range(sp, sp + n):
            mx = max(mx, self.dp(nums, i, n - i))
            mn = min(mn, self.dp(nums, sp + n,))



        # if n == 0 or n == len(nums) - 1:
        #     return -1
        # upper side should be maximum
        mx = 0
        mn = 0
        for i in range(0, n):
            mx = max(mx, self.dp(nums, n - 1))
            mn = min(mn, self.dp(nums, n + 1))
        return mx / mn


        # mx = 0
        # for i in range(0, n):
        #     mx = max(mx, self.dp(nums, n - 1))
        #
        #
        # mn = 99999
        # for i in range(n + 1, len(nums)):
        #     mn = min(mn, self.dp(nums, n + 1))
        #
        #
        #
        #
        # # lower side should be minimum
        #
        # mx = 0
        # for i in range(n, len(nums) - 1):
        #     mx = max(mx, self.dp(nums, n - 1) / )





    # def dp(self, nums, s, f):
    #     if s == len(nums) - 1 or f == 0:
    #         return 1
    #
    #     #if n == len(nums) - 1 or n == 0:
    #     #    return nums[n]
    #     mx = 0
    #     for i in range(s, f):
    #         mx = max(mx, self.dp(nums, s, f - 1) / nums[])
    #         mx = max(mx, self.dp(nums, n - 1) / nums[n] / self.dp(nums, n + 1))
    #     return mx

    def optimalDivision(self, nums):
        if len(nums) == 1:
            return "nums[0]"

        return self.dp(nums, 1)





        """
        :type nums: List[int]
        :rtype: str
        """
