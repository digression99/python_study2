#
# idea 2
# for example, n = 7, k = 5
# start from [1, 2, 3, 4, 5]
# at the last, 5 could be 6, 7, thus [1, 2, 3, 4, 6], [1, 2, 3, 4, 7]
# could be possible.
# if last reaches to n, return to list[(last - 1)] + 1 -> 4 + 1 : 5
# now, increase the second last till n, thus
# [1, 2, 3, 5, 6] ,[1, 2, 3, 5, 7]
# [1, 2, 3, 6, 7]
# could be possible.
#
# now, increase third last till n, thus
# [1, 2, 4, 5, 6], [1, 2, 4, 5, 7]
# [1, 2, 4, 6, 7]
# [1, 2, 5, 6, 7]
# could be possible.
# this implies dp solution.
#
#

# def combine(self, n, k):
#     ans = []
#     stack = []
#     x = 1
#     while True:
#         l = len(stack)
#         if l == k:
#             ans.append(stack[:])
#         if l == k or x > n - k + l + 1:
#             if not stack:
#                 return ans
#             x = stack.pop() + 1
#         else:
#             stack.append(x)
#             x += 1
#
# # 26 / 26 test cases passed.
# # Status: Accepted
# # Runtime: 60 ms
# # 98.51%
class Solution(object):
    def combine(self, n, k):
        l = [] # base list
        ret = []
        #start ->
        for i in range(k):
            l.append(i + 1)
        # n = 6, k = 4 -> 1 2 3 4 -> 1 2 3 5 -> 1 2 3 6 -> 1 2 4 5
        #
        #                 0 1 2 3
        end = k - 1
        while ret[end] + end < n:
            org = l
            while ret[end] <= n:
                pass
                #ret[end] += 1
                #ret.append()

            for j in range(ret[end] + 1, n + 1):
                ret.append(l[:end] + [j] + l[end:])
                ret[end] += 1
            l[end - 1] += 1














class Solution(object):
    #def rec(self, l, start, k, n):
    #    if start == n:
    #        return

    def combine(self, n, k):
        l = []
        for i in range(n):
            l.append([i + 1])
        for i in range(1, k):
            nowlen = len(l)
            for u in range(nowlen):
                t = l.pop(0)
                mx = t[i - 1]

                #mx = 0
                #if len(t) > 1:
                #    mx = max(t)
                #else:
                #    mx = t

                for j in range(mx + 1, n + 1):
                    l.append(t + [j])
        return l

print(Solution().combine(4, 2))