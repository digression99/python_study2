class Solution(object):
    def factorial(self, n):
        if n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def getAnswer(self, n, k):
        return self.factorial(n) / (self.factorial(n - k) * self.factorial(k))

    def numDistinct(self, s, t):
        ans = 0
        i = 0  # idx of s
        j = 0  # idx of t
        dup = 0  # n of redundant char
        cnts = 0
        cntt = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                if i + 1 < len(s):
                    if s[i + 1] == t[j]:
                        cnts += 1
                        i += 1
                    elif s[i + 1] != t[j]:
                        if j + 1 < len(t):
                            if t[j + 1] == s[i + 1]:
                                j += 1
                                cntt += 1
                            elif t[j + 1] != s[i + 1]:
                                ans += self.getAnswer(cnts, cntt)
                                cnts = 0
                                cntt = 0
                else:
                    if j + 1 < len(t):
                        if s[i] == t[j + 1]:
                            j += 1
                            cntt += 1
                    else:
                        if s[i + 1] == t[j + 1]:
                            ans += self.getAnswer(cnts, cntt)
                        else:
                            return 0

            elif s[i] != t[j]:
                if i + 1 < len(s):
                    i += 1
                else:
                    return 0
        return ans

sol = Solution()
print(sol.numDistinct('abc', 'abc'))