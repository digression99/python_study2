class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        x = 2 ** 31

        for i in range(0, 32): # till
            if x ^ n == 0:
                return True
            x >>= 1
        return False
        """
        :type n: int
        :rtype: bool
        """

obj = Solution()
print(obj.isPowerOfTwo(1))
