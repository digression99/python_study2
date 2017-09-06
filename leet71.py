# test = "/abc/abc2/"
# test2 = "/a/./b/..///../c/"
# ret = test.split('/')
# ret2 = test2.split('/')
#
# while '' in ret2:
#     ret2.remove('')
#
# s = '/' + '/'.join(ret2)
#
# print(ret2)
# print(s)


class Solution(object):
    def simplifyPath(self, path):
        t = path.split('/')
        ret = []
        while '' in t:
            t.remove('')
        for i in range(len(t)):
            if t[i] == '.':
                continue
            elif t[i] == '..':
                if len(ret) > 0:
                    ret.pop()
            else:
                ret.append(t[i])

        return '/' + '/'.join(ret)

path = "/a/./b/../../c/"
path2 = "/home/"
path3 = "/../"
path4 = "/home//foo/"
path5 = "/"
obj = Solution()
print(obj.simplifyPath(path5))