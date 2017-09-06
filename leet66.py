class Solution(object):
    def plusOne(self, digits):
        if not digits:
            return None
        s = 0

        for i in range(len(digits)):
            s += digits[i] * (10 ** len(digits) - i - 1))
            s += 1
        l = []
        t = 10 ** (len(digits) - 1)
        while s:
            n = s / t
            s -= n * t
            t /= 10
            l.append(n)
        return l

print(Solution().plusOne([1, 2, 3, 4]))
reversed