# n = int(input())
# dat = list(map(int, input().split()))
#
# #d = [0] * (n + 2)
# mx = -1000
#
# for i in range(n):
#     l, h = i - 1, i + 1
#     s = 0
#     while l >= 0 and dat[l] >= 0:
#         s += dat[l]
#         l -= 1
#     while h <= n - 1 and dat[h] >= 0:
#         s += dat[h]
#         h += 1
#     mx = max(mx, s + dat[i])
# print(mx)

n = int(input())
dat = list(map(int, input().split()))

d = [0] * (n + 2)
d[0] = 0 if dat[0] < 0 else dat[0]
mx = -1000
for i in range(n):
    if i - 1 < 0:
        mx, d[i] = dat[i], dat[i]
        continue
    d[i] = dat[i]
    if d[i - 1] > 0:
        d[i] += d[i - 1]
    #d[i] = max(d[i - 1] + dat[i], 0)
    mx = max(mx, d[i])
print(mx)


