class Solution(object):
    def minDistance(self, word1, word2):
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        ln1 = len(word1)
        ln2 = len(word2)
        pat = ""
        pat = word1 if ln1 < ln2 else word2
        s = ""
        s = word1 if ln1 > ln2 else word1
        mxlen = 0
        patstart = 0
        sstart = 0

        for i in range(len(s)):
            for j in range(len(pat)):
                if pat[j] == s[i]:
                    for k in range(len(pat) - j):
                        if i + k >= len(s) or pat[j + k] != s[i + k]:
                            if mxlen < k - j:
                                mxlen = k + 1
                                sstart = i
                                patstart = j
                            break
                    else:
                        mxlen = k + 1
                        sstart = i
                        patstart = j
        return len(s[:sstart]) + len(s[sstart + mxlen:]) + len(pat[:patstart]) + len(pat[patstart + mxlen:])

w1 = "a"
w2 = "b"


print(Solution().minDistance(w1, w2))
