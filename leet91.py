class Solution(object):

    def dp2(self, s, d, pos):
        if pos >= len(s) - 1:
            return 1
        tot = 0
        #d[pos] = self.dp(s, d, pos + 1)
        tot += 1
        if pos + 1 < len(s) and int(s[pos] + s[pos + 1]) < 27:
            tot += 1
        if tot == 1:
            return self.dp2(s, d, pos + 1)
        else:
            return self.dp2(s, d, pos + 2) + self.dp2(s, d, pos + 1)






    # def dp(self, s, d, pos):
    #     if pos >= len(s) - 1:
    #         return 0
    #     else:
    #         return self.dp(s, d, pos + 1) + self.dp(s, d, pos + 2)
    #
    #     tot = 0
    #     if d[pos] == 0:
    #         d[pos] = 1 + self.dp(s, d, pos + 1)
    #         tot += d[pos]
    #     #tot = 1 + self.dp(s, pos + 1)
    #     if pos + 1 < len(s) and int(s[pos] + s[pos + 1]) < 27:
    #         if d[pos + 1] == 0:
    #             d[pos + 1] = 1 + self.dp(s, d, pos + 2)
    #             tot += d[pos + 1]
    #         #tot += 1 + self.dp(s, pos + 2)
        #return tot

    def numDecodings(self, s):
        if not s:
            return 0
        d = [0] * len(s)
        return self.dp2(s, d, 0)

s = "1212"
s2 = "41"
s3 = "412"
s4 = "1234123"

print(Solution().numDecodings(s4))
