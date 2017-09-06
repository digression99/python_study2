class Solution(object):
    def reverseWords(self, s):

        stop = 0
        prev = 0
        now = 0
        ss = ""
        length = len(s)
        while now < length:
            if now + 1 < length and s[now + 1] != ' ':
                now += 1
                prev += 1
            else:
                if stop > 0:
                    ss += s[now:stop - 1:-1]
                else:
                    ss += s[now::-1]

                # while now >= stop: # now ~ stop
                #     ss += s[now]
                #     now -= 1
                if prev != len(s) - 1:
                    ss += ' '

                prev += 2
                now = prev
                stop = prev
        return ss







        # l = []
        # ans = []
        # for i in range(len(s)):
        #     if i == len(s) - 1:
        #         ans.append(s[i])
        #         for i in range(len(l)):
        #             ans.append(l.pop())
        #         break
        #     if s[i] == ' ':
        #         for i in range(len(l)):
        #             ans.append(l.pop())
        #         ans.append(' ')
        #     else:
        #         l.append(s[i])
        # ss = ""
        # for k in range(len(ans)):
        #     ss += ans[k]
        # return ss

obj = Solution()
print(obj.reverseWords("Let's take LeetCode Contest"))
#
# print(obj.reverseWords("Let's take LeetCode Contest"))