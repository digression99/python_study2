class Solution(object):
    def findCom(self, candidates, start, st, anslist, target):
        if target <= 0:
            anslist.append(st)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue # 값이 같다면 같은 셋이 나오므로 패스
            if candidates[i] > target: # ascending이므로 이게 더 크면 더 진행할 수 없다.
                break
            # st + [candidates[i]] 는 새로운 리스트를 복사해서 보낸다.
            self.findCom(candidates, i + 1, st + [candidates[i]], anslist, target - candidates[i])

    def combinationSum2(self, candidates, target):
        candidates.sort()
        anslist = []
        self.findCom(candidates, 0, [], anslist, target)
        return anslist



# class Solution(object):
#     def findCom(self, anslist, candidates, target):
#         for i in range(len(candidates)): # in fact length of target
#             com = target - candidates[i]
#             if com < 0: break
#             if com == 0:
#                 anslist[target].append([candidates[i]])
#                 break
#             for j in range(len(anslist[com])):
#                 if anslist[com][j][len(anslist[com][j]) - 1] >= candidates[i]:
#                     anslist[target].append(anslist[com][j] + [candidates[i]])
#     def combinationSum(self, candidates, target):
#         candidates.sort()
#         anslist = [[] for i in range(target + 1)]
#         for i in range(1, target + 1):
#             self.findCom(anslist, candidates, i)
#         return anslist[target]

obj = Solution()
print(obj.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))