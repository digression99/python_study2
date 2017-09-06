class Solution(object):
    def findUnsortedSubarray(self, nums):
        mnidx = 9999
        mxidx = 0
        for i in range(len(nums) - 1):
            if nums[i]  > nums[i + 1]:
                for j in range(i + 1, -1, -1):
                    if j - 1 >= 0 and nums[j] < nums[j - 1]:
                        if j - 1 < mnidx:
                            mnidx = j - 1
                        if j > mxidx:
                            mxidx = j
                        nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    else:
                        break
        mnidx = 0 if mnidx == 9999 else mnidx
        mxidx = -1 if mxidx == 0 else mxidx
        return mxidx - mnidx + 1

l1 = [2, 6, 4, 8, 10, 9, 15]
l2 = [2, 6, 4, 4, 8, 10, 9, 15]
l3 = [1, 2, 3, 4]
l4 = [2, 1]

print(Solution().findUnsortedSubarray(l4))

