class Solution(object):
    def subsets(self, nums):
        nums.sort()
        ht = {}
        ans = [[]]
        k = len(nums)
        for i in range(len(nums)):
            ans.append([nums[i]])
            ht.setdefault(nums[i], i)
        l = ans[1:]
        for i in range(1, k):
            nowlen = len(l)
            for u in range(nowlen):
                t = l.pop(0)
                for j in range(ht[t[-1]] + 1, k):
                    ans.append(t + [nums[j]])
                    l.append(t + [nums[j]])
        return ans

ss = [1, 2, 3]
ss2 = [9,0,3,5,7]
print(Solution().subsets(ss2))