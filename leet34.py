class Solution(object):
    def bs(self, nums, l, r, target):
        if l > r:
            return -1

        mid = (l + r ) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.bs(nums, mid + 1, r, target)
        else:
            return self.bs(nums, l, mid - 1, target)

    def leftbs(self, nums, l, r, target):
        # no chance for the number to over the target number
        if l > r:
            return -1
        m = (l + r) // 2
        if nums[m] == target:
            if m - 1 < 0 or nums[m - 1] < target:
                return m
            else:
                return self.leftbs(nums, l, m - 1, target)
        return self.leftbs(nums, m + 1, r, target)
        # elif nums[m] < target:
        #     return self.leftbs(nums, m + 1, r, target)
        # return -1

    def rightbs(self, nums, l, r, target):
        if l > r:
            return -1

        m = (l + r) // 2
        if nums[m] == target:
            if m + 1 > len(nums) - 1 or nums[m + 1] > target:
                return m
            else:
                return self.rightbs(nums, m + 1, r, target)
        elif nums[m] > target:
            return self.rightbs(nums, l, m - 1, target)
        # elif nums[m] > target:
        #     return self.rightbs(nums, l, m - 1, target)
        # return -1

    def searchRange(self, nums, target):
        pos = self.bs(nums, 0, len(nums) - 1, target)
        l = [-1, -1]

        if pos < 0:
            return l
        t = self.leftbs(nums, 0, pos - 1, target)
        l[0] = t if t >= 0 else pos
        t = self.rightbs(nums, pos + 1, len(nums) - 1, target)
        l[1] = t if t >= 0 else pos
        # l[0] = self.leftbs(nums, 0, pos - 1, target) == 1 or
        #
        # l[0] = self.leftbs(nums, 0, pos - 1, target)
        # l[1] = self.rightbs(nums, pos + 1, len(nums) - 1, target)
        return l

obj = Solution()

print(obj.searchRange([1, 1, 1, 1, 1, 1, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8, 8], 8))
#print(obj.searchRange([5, 7, 7, 8, 8, 10], 8))
