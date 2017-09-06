class Solution(object):
    # def __init__(self):
    #     self.length = 0

    # def bs(nums, l, r, target):
    #     # when referencing the array, mod it.
    #     if l > r:
    #         return -1
    #     m = (l + r) // 2
    #     if nums[m % self.length] == target:
    #         return m % self.length
    #     elif nums[m % self.length] > target:
    #         r = m - 1
    #     else:
    #         l = m + 1
    #     return bs(nums, l, r, target)

    def bs(self, nums, l, r, target):
        if l >= r:
            return l if target == nums[l] else -1
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        if nums[l] <= nums[r]:
            # normal binary search
            if nums[mid] < target:
                return self.bs(nums, mid + 1, r, target)
            else:
                return self.bs(nums, l, mid - 1, target)
        else:
            # circular binary search
            if nums[mid] >= nums[l]:
                if nums[l] > target:
                    return self.bs(nums, mid + 1, r, target)
                elif nums[l] < target:
                    if nums[mid] < target:
                        return self.bs(nums, mid + 1, r, target)
                    return self.bs(nums, l, mid - 1, target)
                else:
                    return l
            elif nums[mid] <= nums[r]:
                if nums[r] > target:
                    if nums[mid] > target:
                        return self.bs(nums, l, mid - 1, target)
                    return self.bs(nums, mid + 1, r, target)
                elif nums[r] < target:
                    return self.bs(nums, l, mid - 1, target)
                else:
                    return r
            return -1

    def search(self, nums, target):
        if not nums:
            return -1
        if len(nums) < 2:
            return 0 if nums[0] == target else -1

        return self.bs(nums, 0, len(nums) - 1, target)

        # self.length = len(nums)



        # for i in range(len(nums)):
        #     if target == nums[i]:
        #         return i
        # return -1

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
obj = Solution()
l = [0, 1, 2, 3, 4, 5, 7, 8, 9]
l2 = [7, 8, 9, 0, 1, 2, 4, 5]
l3 = [1, 3]
l4 = [3, 5, 1]
l5 = [4, 5, 6, 7, 8, 1, 2, 3]
print(obj.search(l5, 8))
