class Solution(object):
    def exhaustive(self, ans, s, nowdiv, nowlen, n):
        if nowdiv == 3:
            test = s[nowlen:n + 1]
            if n - nowlen + 1 > 1 and test[0] == "0":
                return False
            if n - nowlen + 1 >= 4 or not 0 <= int(s[nowlen:n + 1]) <= 255:
                return False
            ans.append(s)
            return True
        else:
            for i in range(1, n - nowlen + 1):
                if i < 4:
                    #if i > 1 and s[nowlen + i] == "0":
                    #    return False
                    #if s[nowlen] == "0" and s[nowlen + i] == "0":
                    #    return False
                    test = s[nowlen:nowlen + i]
                    if i > 1 and test[0] == "0":
                        continue
                    if 0 <= int(s[nowlen:nowlen + i]) <= 255:
                        self.exhaustive(ans, s[:nowlen + i] + '.' + s[nowlen + i:], nowdiv + 1, nowlen + i + 1, n + 1)
                else:
                    break
        return False

    def restoreIpAddresses(self, s):
        ans = []
        self.exhaustive(ans, s, 0, 0, len(s) - 1)
        return ans

s1 = "25525511135"
s2 = "010010"
s3 = "0000"
s4 = "00000"

print(Solution().restoreIpAddresses(s1))

