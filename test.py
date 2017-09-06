class Solution(object):
    def singleNumber(self, nums):
        i = 0
        j = i + 1
        l = len(nums) - 1

        while True:
            if i == l:
                return nums[i]
            if nums[j] == -1:
                continue
            if nums[i] == -1:
                i += 1
                j = i + 1
            elif nums[i] == nums[j]:
                nums[i] = nums[j] = -1
                i += 1
                j = i + 1
            elif nums[i] != nums[j]:
                if j == l:
                    return nums[i]
                j += 1
        # you have to deal with the negative num.


        """
        :type nums: List[int]
        :rtype: int
        """
