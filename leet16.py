class Solution(object):
    def threeSumClosest(self, nums, target):
        if not nums or len(nums) < 3:
            return target
        # closest -> min difference.

        nums.sort()
        mindif = 99999
        minsum = 99999
        for i in range(len(nums) - 2):
            l = i + 1
            h = len(nums) - 1
            while l < h:
                s = nums[i] + nums[l] + nums[h]
                dif = abs(s - target)

                if mindif > dif:
                    mindif = dif
                    minsum = s

                if target > s:
                    l += 1
                elif target < s:
                    h -= 1
                else: #(target == s)
                    return target
        return minsum

                # if mindif < dif:
                #     l += 1
                #     h -= 1
                # elif mindif < dif: # how to manipulate l and h?
                #     l += 1
                # else: # mindif == dif -> how to manipulate l and h?
                #     return 0

obj = Solution()
S = [-1, 2, 1, -4]
tgt = 1

print(obj.threeSumClosest(S, tgt))