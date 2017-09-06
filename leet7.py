class Solution(object):
    def reverse(self, x):
        l = []
        s = False
        ans = 0
        if x < 0:
            s = True
            x = -x

        while x > 0:
            l.append(x % 10)
            x //= 10

        i = 0
        while l:
            ans += int(l.pop()) * pow(10, i)
            i += 1

        if s:
            ans = -ans

        if ans > pow(2, 31) - 1 or ans < -pow(2, 31):
            return 0

        return ans

s = "abcdefg"
#
# print(s[::2])
# print(-123 % 10)
#
# print(-10 % 100)
# print(-1234 % 10)

print(-7 % 10)

print(-7 % 3)
print(7 % 3)
value = 10
print(f'string is {value * 20}')
print('string is ' + repr(value * 20)[::-1])