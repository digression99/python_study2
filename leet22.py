class Solution(object):
    def getPar(self, l, val, numlist, n):
        if val == n:
            if numlist not in l:
                l.append(numlist)
            return
        for i in range(1, n + 1):
            if val + i <= n:
                self.getPar(l, val + i, numlist + str(i), n)

    def generateParenthesis(self, n):
        d = [[] for i in range(n + 1)]
        l = []
        d[1].append('()')

        for i in range(2, n + 1):
            for j in range(len(d[i - 1])):
                d[i].append('(' + d[i - 1][j] + ')')
            self.getPar(l, 0, "", i)
            for _ in range(len(l)):
                s = l.pop()
                par = ""
                for k in range(len(s)):
                    par += '(' * int(s[k]) + ')' * int(s[k])
                if par not in d[i]:
                    d[i].insert(0, par)
            l.clear()
        return d[n]









        # l = []
        # val = 0
        # numlist = ""
        # self.getPar(l, val, numlist, n)
        #
        # for _ in range(len(l)):
        #     s = l.pop()
        #     par = ""
        #     for i in range(len(s)):
        #         par += '(' * int(s[i]) + ')' * int(s[i])
        #     l.insert(0, par)
        # return l






obj = Solution()
print(obj.generateParenthesis(4))