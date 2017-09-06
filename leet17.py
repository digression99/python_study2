class Solution(object):
    def makeCom2(self, l1, l2):
        #init -> l1 : empty, l2 : list of list
        if len(l2) == 0:
            return l1

        l3 = []

        for i in range(len(l1)):
            for j in range(len(l2[0])):
                if l1[i] != '$' and l2[0][j] != '$':
                    l3.append(l1[i] + l2[0][j])

        return self.makeCom2(l3, l2[1:])

        # for i in range(len(l2[0])):
        #     for j in range(len(l1) + 1):
        #         l3.append(l1[i] + l2[j])
        # return self.makeCom2(l3, l2[1:])


    #
    # def makeCom(self, l, end):
    #     if len(l) == 1:
    #         return l[end]
    #     return [i for i in self.makeCom(l, end + 1)]
    #     #return [[i for i in l[0] if i != '$'] for j in ['a', 'b', 'c']]#self.makeCom(l[1:]) if j != '$']

    def letterCombinations(self, digits):
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        l = [['$']for i in range(len(digits))]
        #l = ['$'] * len(digits)
        #ans = []

        for i in range(len(digits)):
            for j in d[digits[i]]:
                l[i].insert(0, j)

        return self.makeCom2(l[0], l[1:])
        # for i in digits:
        #     l.append(d[i])
        #
        # for j in l:











        """
        :type digits: str
        :rtype: List[str]
        """
obj = Solution()
print(obj.letterCombinations('2345'))
#print(list(map(lambda x, y : x + y, ['a', 'b', 'c' ,'d'], ['e', 'f', 'g'])))