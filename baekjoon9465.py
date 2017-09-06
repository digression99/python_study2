tc = int(input())

def dp(d, a, n, m):
    if n == 1:
        return d[n][m]

    if d[n][m] > 0:
        return d[n][m]

    if m == 0:
        d[n][0] = max(dp(d, a, n - 1, 0), dp(d, a, n - 1, 1), dp(d, a, n - 1, 2))
    elif m == 1:
        d[n][1] = max(dp(d, a, n - 1, 0), dp(d, a, n - 1, 2)) + a[n - 1][0]
    elif m == 2:
        d[n][2] = max(dp(d, a, n - 1, 0), dp(d, a, n - 1, 1)) + a[n - 1][1]

    return max(d[n][0], d[n][1], d[n][2])

for i in range(tc):
    n = int(input())
    d = [[0] * 3 for u in range(n + 3)]
    a = [[0] * (n + 2) for v in range(2)]

    for j in range(2):
        resp = input()
        pce = resp.split()
        for k in range(n):
            a[k][j] = int(pce[k])

    ans = max(dp(d, a, n, 0), dp(d, a, n, 1), dp(d, a, n, 2))
    print(ans)








