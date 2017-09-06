class Solution(object):
    def longestPalindrome(self, s):
        count = 0
        mxcount = 0
        mid = 0
        isEven = False
        for i in range(0, len(s)):
            for j in range(1, len(s) - i):
                if i - j >= 0:
                    if s[i - j] != s[i + j]:
                        break
                    count += 1

            if isEven and mxcount < count + 1:
                mid = i
                mxcount = count
                isEven = False
            if not isEven and mxcount < count:
                mid = i
                mxcount = count
                isEven = False
            count = 0

            for j in range(0, len(s) - i):
                if i + j + 1 < len(s) and i - j >= 0:
                    if s[i - j] != s[i + j + 1]:
                        break
                    count += 1

            if mxcount < count:
                mid = i
                mxcount = count
                isEven = True
            count = 0
        if isEven:
            return s[mid - mxcount + 1:mid + mxcount + 1]
        return s[mid - mxcount:mid + mxcount + 1]