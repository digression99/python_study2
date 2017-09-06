class Solution(object):
    def checkRecord(self, s):
        acnt = 0
        contl = 0
        for i in range(len(s)):
            if s[i] == 'A':
                acnt += 1
                if acnt > 1:
                    return False
            if s[i] == 'L':
                contl += 1
                if contl > 2:
                    return False
            cntl = 0
        return True

obj = Solution()

s = "PPALLL"
print(obj.checkRecord(s))