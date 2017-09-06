class Solution(object):
    def sumsum(self, ans, nums, target, i, j):
        if i >= j:
            return

        while i < j:
            k, l = i + 1, j - 1
            min, max = 123456789, -123456789
            s = nums[i] + nums[j] + nums[k] + nums[l]
            while k < l:
                if s < min:
                    min = s
                if s > max:
                    max = s

                if s < target:
                    k += 1
                elif s > target:
                    l -= 1
                else:
                    lis = [nums[i], nums[j], nums[k], nums[l]]
                    if lis not in ans:
                        ans.append(lis)
                        #ans.append([nums[i], nums[j], nums[k], nums[l]])
                        #ans.insert(0, [nums[i], nums[j], nums[k], nums[l]])
                        #ans.append([nums[i], nums[j], nums[k], nums[l]])
                    # while k < l and nums[k] == nums[k + 1]:
                    #     k += 1
                    # while k < l and nums[l] == nums[l - 1]:
                    #     l -= 1
                    k += 1
                    l -= 1
                s = nums[i] + nums[j] + nums[k] + nums[l]
            # while i < j and nums[i] == nums[i + 1]:
            #     i += 1
            # while i < j and nums[j] == nums[j - 1]:
            #     j -= 1
            if max < target:
                i += 1
            elif min > target:
                j -= 1
            else: # min < target < max
                self.sumsum(ans, nums, target, i + 1, j)
                self.sumsum(ans, nums, target, i, j - 1)
                break

    def fourSum(self, nums, target):
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = []

        self.sumsum(ans, nums, target, 0, len(nums) - 1)
        return ans

obj = Solution()
#print(obj.fourSum([1, 0, -1, 0, -2, 2], 0))

# [-1,-5,-5,-3,2,5,0,4]
# -7
#print(obj.fourSum([-3, -1, 0, 2, 4, 5], 2))
print(obj.fourSum([-1,-5,-5,-3,2,5,0,4], -7))
