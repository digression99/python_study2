class Solution(object):
    # class TreeNode(object):
    #     def __init__(self, ch):
    #         self.data = ch
    #         self.nodelist = []
    #     def insertChildNode(self, cnode):
    #         self.nodelist.append(cnode)

    def groupAnagrams(self, strs):
        import copy
        dl = []  # dict list
        ans = []  # real list
        cnt = 0
        for i in range(len(strs)):
            tempd = {}
            for j in range(len(strs[i])):
                tempd.setdefault(strs[i][j], 0)
                tempd[strs[i][j]] += 1

            k = 0
            while k < len(dl):
                if set(tempd.items()) == set(dl[k].items()):
                    ans[k].append(strs[i])
                    break
                k += 1
            if k == len(dl):
                cnt += 1
                ans.append([])
                ans[cnt - 1].append(strs[i])
                # tempd[0] = cnt
                dl.append(copy.deepcopy(tempd))
            tempd.clear()




            # for k in range(len(dl)):
            #     if set(tempd.items()) == set(dl[k].items()):
            #         ans[k].append(strs[i])
            #     else:
            #         cnt += 1
            #         ans.append([])
            #         ans[cnt - 1].append(strs[i])
            #         #tempd[0] = cnt
            #         dl.append(copy.deepcopy(tempd))
            #         break
            # tempd.clear()
        return ans

obj = Solution()
strs = ["abc", "cba", "sbe", "ebs"]
print(obj.groupAnagrams(strs))