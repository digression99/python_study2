
# #first try
# n = int(input())
# memo = [0] * (n + 2)
#
# memo[1] = 9
# memo[2] = 17
# stn = 8 # start num
# for i in range(3, n + 1):
#     memo[i] += memo[i - 1] + (stn - i + 2)
#     for j in range(0, i - 2):
#         memo[i] += (stn - j) * (2 ** (i - j - 3))
# print(memo[n])

# for (int i=1; i<=9; i++) d[1][i] = 1LL;
# for (int i=2; i<=n; i++) {
#     for (int j=0; j<=9; j++) {
#         d[i][j] = 0;
#         if (j-1 >= 0) d[i][j] += d[i-1][j-1];
#         if (j+1 <= 9) d[i][j] += d[i-1][j+1];
#         d[i][j] %= mod;
# } }
# long long ans = 0;s
# for (int i=0; i<=9; i++) ans += d[n][i];
# ans %= mod;

mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for j in range(0, 5)]
#print(mat)
mat[0][0] = 1
print(mat)
