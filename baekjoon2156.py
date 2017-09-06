n = int(input())

dat = [0] * 10001
d = [0] * 10001
#d = [[0] * 2 for _ in range(n + 3)]

for j in range(1, n + 1):
    dat[j] = int(input())

d[0] = 0
d[1] = dat[1]
d[2] = dat[1] + dat[2]

for i in range(3, n + 1):
    d[i] = max(d[i - 1], d[i - 2] + dat[i], d[i - 3] + dat[i] + dat[i - 1])

    # d[i] = d[i - 1]
    # if d[i] < d[i - 2] + dat[i]:
    #     d[i] = d[i - 2] + dat[i]
    # if d[i] < d[i - 3] + dat[i] + dat[i - 1]:
    #     d[i] = d[i - 3] + dat[i] + dat[i - 1]
print(d[n])





#
# cnt = 0
#
#
#
# d[1][0] = dat[1]
# d[1][1] = 0
# d[2][0] = max(d[1][0], d[1][1]) + dat[2]
# d[2][1] = max(d[1][0], d[1][1])
#
# d[3][0] = 0
# d[3][1] = max(d[2][0], d[2][1])
# d[4][0] = max(d)
#
# for i in range(1, n + 1):
#     if cnt < 3:
#         d[i][0] = d[i - 1][0] + d[i - 1][1]
#
#
#
# def dp(dat, d, n, cnt):
#     if cnt == 2:
#         cnt = 0
#         d[n][0] = 0
#         d[n][1] = dp(dat, d, n - 1, cnt)
#         return
#     else:
#         if n == 1:
#             return
#         pass