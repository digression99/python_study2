class Solution(object):
    # def grayCode(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[int]
    #     """
    #     res = []
    #     size = (1 << n)
    #     for i in range(size):
    #         res.append((i >> 1) ^ i)
    #     return res
    def grayCode(self, n):
        if n == 0:
            return [0]
        l = [0, 1]
        start = '1'

        for i in range(n - 1):
            start += '0'
            for j in range(len(l) - 1, -1, -1):
                l.append(int(start, 2) + l[j])
        return l

print(Solution().grayCode(3))


