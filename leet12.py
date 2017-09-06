class Solution(object):
    def intToRoman(self, num):
        v = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        n = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        str = ""
        i = len(v) - 1
        while num > 0:
            val = num // v[i]
            str += (n[i] * val)
            num = num % v[i]
            i -= 1
        return str


obj = Solution()
print(obj.intToRoman(3328))