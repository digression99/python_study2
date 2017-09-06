class Solution(object):
    def findCom(self, anslist, candidates, target):
        for i in range(len(candidates)): # in fact length of target
            com = target - candidates[i]
            if com < 0: break
            if com == 0:
                anslist[target].append([candidates[i]])
                break
            #if com not in candidates: # 4 -> 2 2 일 때를 처리 못한다...
            # duplicate 처리해야.
            #if com >= candidates[i]: -> 2 / 5, 3/ 4 일때 duplicate 발생
            for j in range(len(anslist[com])):
                if anslist[com][j][len(anslist[com][j]) - 1] >= candidates[i]:
                    anslist[target].append(anslist[com][j] + [candidates[i]])
    def combinationSum(self, candidates, target):
        candidates.sort()
        anslist = [[] for i in range(target + 1)]
        for i in range(1, target + 1):
            self.findCom(anslist, candidates, i)
        return anslist[target]

obj = Solution()
print(obj.combinationSum([2, 3, 6, 7], 7))






                    #[candidates[i], anslist[com][j]])
                                            #2, 2
# anslist
#[0] -> []
#[1] -> []
#[2] -> [2]
#[3] -> [3]
#[4] -> [
#           [2, 2]
#       ]
#[5] -> [
#           [3, 2]
#
#
#       ]
#[6] -> [
#                [2 2 2] -> com = 4 <= candidates[i]=2 일때 처리 안됨.
#                [3 3]
#                [6]
#[7] -> [
#                [3 2 2] # candidates[i] = 2 -> com = 5
#                [2 2 3] # candidates[i] = 3 -> com = 4
#                [7]

# testl = [1, 2, 3, 4]
# testlist = [[]] * 10
# testlist[0].append(1)
# # testlist[0].append(12)
# # testlist.append([1, 2, 3])
# #print(testlist)
# if 3 in testl:
#     print("t")
# print("f")
#comblist = [1, testlist]
#print(comblist)