# add binary

class Solution(object):
    def addBinary(self, a, b):
        ret = []
        c = 0
        s = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            ai = 0 if i < 0 else int(a[i])
            bi = 0 if j < 0 else int(b[j])
            ret.insert(0, ai ^ bi ^ c)
            c = 1 if ai + bi + c > 1 else 0
            i -= 1
            j -= 1
        if c == 1:
            ret.insert(0, c)
        return ''.join(str(e) for e in ret)

a = "1001"
b = "101"
print(int(a, 2)) # int(a, 2) -> a가 2진법이고 그것을 int로 바꾼다.
print(bin(int(a, 2) + int(b, 2))[2:])


#print(Solution().addBinary("1", "1"))
#print(''.join(str(e) for e in ret))
