
#try1
# n = int(input())
#
# dat = []
# for i in range(n):
#     dat.append(int(input()))

# dat.reverse()
#
# d = [[0] * 2 for _ in range(n + 1)]
# d[0][0], d[0][1] = 0, 0
# d[1][0], d[1][1] = 0, dat[0]
# for i in range(2, n + 1):
#     d[i][0] = d[i - 1][1]
#     d[i][1] = max(d[i - 2][0] + dat[i - 2], d[i - 2][1]) + dat[i - 1]
#
# print(max(d[n][0], d[n][1]))


# d[1][0] = dat[0]
# for i in range(2, n + 1):
#     d[i][1] = d[i - 1][0] + dat[i - 1]
#     d[i][0] = max(d[i - 2][0], d[i - 2][1]) + dat[i - 1]
#
# print(max(d[n][0], d[n][1]))

# 10
# 1231
# 5223
# 10000
# 2323
# 8765
# 9625
# 1236
# 12
# 247
# 935

# 10
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1








# try2
# d = [[0] * 2 for _ in range(n + 2)]
# # d[0][0], d[0][1], d[1][0], d[1][1] = 0, 0, 0, 0
# # for calculation
# # 일단 원래 생각대로 코드를 짠 뒤에 인덱스에 맞게 바꾼다.
# for i in range(2, n + 2):
#     if d[i - 2][0] < d[i - 2][1]:
#         d[i][0] -= dat[i - 2]
#     d[i][0] = dat[i - 1] + max(d[i - 2][1], d[i - 2][0]) # not stepped, xox vs oox
#     d[i][1] = max(dat[i - 1] + d[i - 2][0], d[i - 2][1]) + dat[i] # stepped, xoo vs oxo
#
# print(d[n + 1][1])


n = int(input())

dat = []
for i in range(n):
    dat.append(int(input()))
d = [[0] * 2 for _ in range(n + 2)]
d[1][0] = dat[0]
for i in range(2, n + 1):
    d[i][1] = d[i - 1][0] + dat[i - 1]
    d[i][0] = max(d[i - 2][0], d[i - 2][1]) + dat[i - 1]

print(max(d[n][0], d[n][1]))



