#
# def getInc(l1, l2, ans):
#     if len(l2) == 0:
#         return ans
#     for i in l1:
#         for j in l2[0]:
#             if i <= j:
#                 ans += 1
#     return getInc(l2[0], l2[1:], ans)
#
# n = int(input())
# if n == 1:
#     print(10)
# else:
#     l = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(n)]
#     print(getInc(l[0], l[1:], 0))

# dat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(1001)]
#
# n = int(input())
# ans = 0
#
# for i in range(10):
#     dat[1][i] = 1
#
# for i in range(2, n + 1):
#     for j in range(10):
#         for k in range(j + 1): # for m range(10):
#             dat[i][j] += dat[i - 1][k] # dat[i][j] += dat[i -1][9 - m]
#
# # 중복순열 ????????????
# # 중복조합
#
# #    0   1   2   3   4   5   6   7   8   9
# #1   1   1   1   1   1   1   1   1   1   1
# #2   9   8   7                           1
# #3
# #4
# #5
# #6
# #7
# #8
# # ..
#
# for i in range(10):
#     ans += dat[n][i]
# print(ans % 10007)

#n, k -> n : 0 ~9 가짓수 -> 10
# k => 자리수

#((n + k - 1) * (n + (k - 1) - 1) * (n + (k - 2) - 1) * ... (n)) / k!

k = int(input())

print(
    int((((9 + k) * (8 + k) * (7 + k) * (6 + k) * (5 + k) * (4 + k) * (3 + k) *
    (2 + k) * (1 + k)) / 362880) % 10007))


#
# ans = 1
#
# def fac(k):
#     if k == 2:
#         return 1
#     return k * fac(k - 1)
#
# for i in range(k + 9, 10, -1):
#     ans *= i
#
# ans /= k
# print(ans)












































