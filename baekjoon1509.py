#
# 모든 원소는 최대한 될 수 있는 가장 큰 펠린드롬이 되어야 한다.
#
#

#BBCDDECAECBDABADDCEBACCCBDCAABDBADD

s = input()
n = len(s)
d = [[0] * (n + 1) for i in range(n + 1)]#[n + 1][n + 1] # index : 1 ~ n

for i in range(1, n + 1):
    d[i][i] = 1
for i in range(1, n):
    if s[i - 1] == s[i]:
        d[i - 1][i] = 1
for k in range(2, n): # 길이를 늘려나가면서
    for i in range(1, n - k + 1): # 그 길이까지 해당되는 모든 팰린드롬 찾기.
        j = i + k
        if s[i - 1] == s[j - 1] and d[i + 1][j - 1]:
            d[i][j] = 1
print(d)
min()
for i in range(1, n + 1):
    mx = d[1][n]





# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if d[i][j] > 0: # memo
#             continue
#         if s[i] != s[j]: # diffrent two edges
#             d[i][j] = 0 # 1 3 1 1
#             continue # AA
#         if i + 1 <= j - 1:
#             d[i][j] = d[i + 1][j - 1]
#         else:
#             d[i][j] = 1
#
#         #d[i][j] = #d[i + 1][j - 1]
#         if d[i + 1][j - 1] == 0:
#             d[i][j] = 0
#         else:
#
#
#         pass






