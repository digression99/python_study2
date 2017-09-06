class Solution(object):
    def __init__(self):
        self.ans = 0
        self.sChCount = {}
        self.tChCount = {}

    def numDistinct(self, s, t):
        if len(s) == 0 and len(t) == 0:
            return

        if len(s) == 0 and len(t) > 0:




        return ans + numDistinct(s[i + 1:len(s)])