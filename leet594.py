class Solution(object):

    def findLHS(self, nums):
        if not nums:
            return 0
        ret = 0
        for i in range(len(nums)):
            mx = 0
            nown = 1
            check = False
            for j in range(i + 1, len(nums)): # 클때 돈다
                if nums[i] == nums[j]:
                    nown += 1
                if nums[i] - 1 == nums[j]:
                    nown += 1
                    check = True
            if check and mx < nown:
                mx = nown
            nown = 1
            check = False
            for j in range(i + 1, len(nums)):
                if nums[i] + 1 == nums[j]:
                    nown += 1
                    check = True
            if check and mx < nown:
                mx = nown
            if ret < mx:
                ret = mx
        return ret

    # def findLHS(self, nums):
    #     if not nums:
    #         return 0
    #     d = [[1] * 4 for i in range(len(nums))]
    #     mx = 0
    #     mxidx = 0
    #     for i in range(len(nums)):
    #         d[i][0], d[i][1], d[i][2], d[i][3] = 1, 1, 0, False
    #
    #     for i in range(len(nums)):
    #         for j in range(0, i):
    #             if nums[j] == nums[i] - 1:
    #                 d[j][0] += 1
    #
    #                 if not d[j][3]:
    #                     d[j][3] = True
    #
    #                 if mx < d[j][0]:
    #                     mx = d[j][0]
    #                     mxidx = j
    #
    #             if nums[j] == nums[i] + 1:
    #                 d[j][1] += 1
    #
    #                 if not d[j][3]:
    #                     d[j][3] = True
    #
    #                 if mx < d[j][1]:
    #                     mx = d[j][1]
    #                     mxidx = j
    #
    #             if nums[j] == nums[i]:
    #                 d[j][2] += 1
    #                 #if mx < d[j][0] + d[j][2] or mx < d[j][1] + d[j][2]:
    #
    #     # if d[mxidx][3]:
    #     #     mx += d[mxidx][2]
    #
    #     return mx





    # def findLHS(self, nums):
    #     d = [[1] * 2 for i in range(len(nums))]
    #     mx = 0
    #     add = 0
    #
    #     for i in range(len(nums)):
    #         d[i][1] = False
    #
    #     # for i in range(len(nums)):
    #     #     d[i][0] = 1
    #     #     d[i][1] = 1
    #
    #     for i in range(1, len(nums)):
    #         for j in range(0, i):
    #             if nums[j] == nums[i] - 1:
    #                 add = -1
    #
    #             if (nums[j] == nums[i] - 1 or nums[i] + 1 == nums[j]) or \
    #                 d[j][1] and nums[i] == nums[j]:
    #                 d[j][0] += 1
    #                 if not d[j][1]:
    #                     d[j][1] = True
    #                 if mx < d[j][0]:
    #                     mx = d[j][0]
    #
    #             # if nums[j] == nums[i] or nums[i] - 1 == nums[j]:
    #             #     d[j][0] += 1
    #             #     if mx < d[j][0]:
    #             #         mx = d[j][0]
    #     return mx

# class Solution(object):
#     def findLHS(self, nums):
#         d = [[0] * 2 for i in range(len(nums))]
#         mx = 0
#
#         for i in range(len(nums)):
#             d[i][0] = 1
#             d[i][1] = 1
#
#         for i in range(1, len(nums)):
#             for j in range(0, i):
#                 if nums[j] == nums[i] or nums[i] + 1 == nums[j]:
#                     d[j][1] += 1
#                     if mx < d[j][1]:
#                         mx = d[j][1]
#                 if nums[j] == nums[i] or nums[i] - 1 == nums[j]:
#                     d[j][0] += 1
#                     if mx < d[j][0]:
#                         mx = d[j][0]
#         return mx

l = [1, 3, 2, 2, 5, 2, 3, 7]
l2 = [1, 1, 1, 1]
l3 = [1,2,1,3,0,0,2,2,1,3,3]
l4 = [0,3,1,3,3,3,0,1,0,2,0,3,1,3,-3,2,0,3,1,2,2,-3,2,2,3,3]
l5 = [1,3,2,2,5,2,3,7]
l6 = [1, 2, 2, 1]

print(Solution().findLHS(l4))
