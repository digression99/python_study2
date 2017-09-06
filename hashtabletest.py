# D = {}
#
#
#
# D['a'] = 1
# D['b'] = 2
# D['c'] = 3
#
# D['b'] = 4
#
#
# for k in D.keys():
#     print(D[k])
#
# for k, v in D.items():
#     print(k, v)
import random






# making hashtable
D = {}
for i in range(0, 10):
    D[i] = []

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

def twoSum(nums, target):
    if len(nums) <= 1:
        return False

    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i] # 두 수의 인덱스 위치
        else:
            buff_dict[target - nums[i]] = i # how about collision?




def twoSum2(nums, target): # collision 해결 list로
    if len(nums) <= 1:
        return False

    buff_dict = {}
    for i in range(0, 10):
        buff_dict[i] = []

    for i in range(len(nums)):
        hs = (target - nums[i]) % 10
        if hs in list(buff_dict[hs]):
            idx = buff_dict[hs].index(nums[i])
            return [hs, idx, i]
        else:
            buff_dict[nums[i] % 10].append(i)

def twoSum22(nums, target):
    if len(nums) <= 1:
        return False

    hst = []
    for i in range(0, 10):
        hst[i] = []




nums = []

for i in range(0, 100):
    nums.append(int(random.random() * 100))

print(nums)

idx1, idx2, idx3 = twoSum2(nums, 10)

print(idx1, idx2, idx3)











# def fibonacci_func(n):
#     a,b = 0, 1
#     i = 0
#     while True:
#         if (i > n):
#             return
#         yield a
#         a, b = b, a+b
#         i += 1
#
# fib = fibonacci_func(10)
# for x in fib:
#     print(x)
