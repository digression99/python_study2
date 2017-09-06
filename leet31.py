class Solution(object):
    def nextPermutation(self, nums):
        # i = len(nums) -

        # for u in range(i - 1, 0, -1):
        #     if nums[u] < nums[i]:
        #         nums[u], nums[i] = nums[i], nums[u]
        length = len(nums) - 1
        i = length
        while i > 0:
            if nums[i - 1] < nums[i]:
                min = i
                for j in range(i + 1, length + 1):
                    if nums[i - 1] < nums[j] < nums[min]:
                        min = j
                nums[min], nums[i - 1] = nums[i - 1], nums[min]
                nums[i : length + 1] = sorted(nums[i : length + 1])
                return
            else:
                i -= 1
        # length = len(nums) - 1
        # i = length - 1 if length > 0 else 0
        #
        # while i > 0:
        #     if nums[i - 1] < nums[i]:
        #         for j in range(i + 1, length):
        #             if nums[i - 1] < nums[j] < nums[i]:
        #                 nums[i - 1], nums[j] = nums[j], nums[i - 1]
        #                 if i == 1:
        #                     nums.sort()
        #                 else:
        #                     nums[i: length + 1] = sorted(nums[i: length + 1])
        #                     return
        #     i -= 1

            # if i == 1:
            #     nums.sort()
            # else:
            #     nums[i : length + 1] = sorted(nums[i : length + 1])


            # for j in range(length, i, -1):
            #     max = j
            #     for k in range(j - 1, i, -1):
            #         if nums[max] < nums[k]:
            #             max = k
            #     nums[max], nums[j] = nums[j], nums[max]
        #      3 6 5 4
        #      4 6 5 3
        #    ->4 3 5 6
        #      i i+1
        #
        #

obj = Solution()
obj.nextPermutation([2, 3, 1])