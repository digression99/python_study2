
def dp(n, k):
    if k == 1: return 1
    d = [[0] * (n + 1) for i in range(k + 1)]
    for i in range(n + 1): d[1][i] = 1

    for i in range(2, k + 1):
        for j in range(n + 1):
            for u in range(j + 1):
                d[i][j] += d[i - 1][u]
    return d[k][n]

inp = list(map(int, input().split()))
print(dp(inp[0], inp[1]))

