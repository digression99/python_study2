n = int(input())
dat = list(map(int, input().split()))

d = [[0] * 2 for i in range(n)]

# increasing subsequence
for i in range(n):
    mx = 0
    for j in range(i):
        if dat[j] < dat[i]:
            mx = max(mx, d[j][0])
    d[i][0] = mx + 1

#decreasing subsequence
for i in range(n - 1, -1, -1):
    mx = 0
    for j in range(n - 1, i, -1):
        if dat[j] < dat[i]:
            mx = max(mx, d[j][1])
    d[i][1] = mx + 1

mx = 0
for i in range(n):
    mx = max(mx, d[i][0] + d[i][1] - 1)
print(mx)