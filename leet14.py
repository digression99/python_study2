class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        d = {}
        for i in range(0, len(strs)):
            if len(strs[i]) == 0:
                d.setdefault("", 0)
                d[""] += 1
                continue
            for j in range(1, len(strs[i]) + 1):
                d.setdefault(strs[i][0:j], 0)
                d[strs[i][0:j]] += 1

        d = sorted(d.items(), key=lambda x: len(x[0]), reverse=True)
        for i in range(len(d)):
            if d[i][1] == len(strs):
                return d[i][0]
        return ""


        #d.setdefault(, )
        """
        :type strs: List[str]
        :rtype: str
        """

obj = Solution()

l = ["a", "abc", "abcd", "abcde"]
l2 = ["aa", "ab"]
l3 = ["a"]
l4 = [""]
l5 = ["aa", "aa"]
print(obj.longestCommonPrefix(l5))