# def dp(n):
#     if n == 1:
#         return p[1]
#     if memo[n] > 0:
#         return memo[n]
#     mx = p[n]
#     for i in range(1, n):
#         mx = max(mx, p[i] + dp(n - i))
#         if mx > memo[n]:
#             memo[n] = mx
#     return mx

n = int(input())
res = input()
spl = res.split()
p = [0] * (n + 1)
memo = [0] * (n + 1)

for i in range(n):
    p[i + 1] = int(spl[i])

mx = p[1]
memo[1] = p[1]

#4
#1 5 6 7 -> 10 2 / 2
# 1 6 7 10
#memo -> 0 1 2 3 4
#        0 1 6

# 3 -> 3 vs 2 1

for i in range(2, n + 1):
    for j in range(0, i):
        memo[i] = max(memo[i], memo[j] + p[i - j])


        # mx = memo[j] + p[i - j]
        # if memo[i] < mx:
        #     memo[i] = mx
        #     mx = memo[i]
print(memo[n])

