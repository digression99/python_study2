class Solution(object):
    def isValid(self, s):
        if not s or len(s) < 2:
            return False
        st = []
        d = {'(' : ')', '{' : '}', '[' : ']'}

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                st.append(s[i])
            else:
                if len(st) < 1:
                    return False
                ch = st.pop()
                if d[ch] != s[i]:
                    return False
        if len(st) == 0:
            return True
        return False


        """
        :type s: str
        :rtype: bool
        """


obj = Solution()
str = "(("

print(obj.isValid(str))

