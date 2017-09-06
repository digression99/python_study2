class Solution(object):
    def threeSum(self, nums):
        # brute force
        l = []
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tl = [nums[i], nums[j], nums[k]]
                        #s = {nums[i], nums[j], nums[k]}
                        if tl not in l:
                            l.append(tl)
        u = 0
        v = u + 1
        end = len(l)
        while True:
            if set(l[u]) == set(l[v]):
                l.remove(l[v])
                end -= 1
            v += 1
            if v == end - 1:
                u += 1
                v = u + 1
            if u == end:
                break
        return l
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

obj = Solution()
l = [-1, 0, 1, 2, -1, 4]

l2 = obj.threeSum(l)
print(l2)
# 의석스
#     class Solution(object):
# def threeSum(self, nums):
#     result = set()
#     num_dict = {}
#     nums = sorted(nums)

#     for idx, num in enumerate(nums):
#         if num_dict.get(num,0) > 3:
#             continue
#         for x in list(num_dict):
#             if (2 * x == -1 * num):
#                 if num_dict.get(x) > 1:
#                     result.add((x, x, num))
#             else:
#                 if num_dict.get(-num - x):
#                     result.add((min(x, -num - x), max(x, -num-x), num))
#         num_dict[num] = num_dict.get(num, 0) + 1

#     return list(map(lambda triplet: list(triplet), list(result)))