class Solution(object):
    def leastBricks(self, wall):
        ans = 99999
        linenum = 0
        for c in range(len(wall[0])):
            linenum += wall[0][c]

        for i in range(1, linenum): # now line -> i
            maxnum = len(wall)
            for j in range(len(wall)):
                sumnum = 0
                for k in range(len(wall[j])):
                    if sumnum == i:
                        maxnum -= 1 # no need to add more
                        break
                    elif sumnum < i:
                        sumnum += wall[j][k] # need to add more
                    elif sumnum > i: # no need to add more
                        break
            if maxnum < ans:
                ans = maxnum
        if ans == 99999:
            return len(wall)
        else:
            return ans






        # for i in range(len(wall[0])):  # line num -> i + 1
        #     for j in range(len(wall)):
        #         sumnum = 0
        #         for k in range(len(wall[j])):












            # d = {}
            # maxnum = 0
            # for j in range(len(wall)):  # row num
            #     sumnum = 0
            #     for k in range(0, i + 1):  # col num
            #         sumnum += wall[j][k]
            #     #cross = d.setdefault(j, 0)
            #     if sumnum in d.values():
            #         maxnum += 1
            #     else:
            #         d[j] = sumnum
            #
            # if ans > maxnum:
            #     ans = maxnum
        #return ans

obj = Solution()

l = [[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
l2 = []
l3 = [[100000000],[100000000],[100000000]]
l2.append([1])
#print(obj.leastBricks(l))
print(obj.leastBricks(l3))