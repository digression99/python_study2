inp = input().split()
n, m = int(inp[0]), int(inp[1])

mat = [[0] * m for i in range(n)]
#d = [[0] * m for i in range(n)]

for i in range(n):
    inp = list(map(int, input().split()))
    for j in range(m):
        mat[i][j] = int(inp[j])

t = mat[0][0]

for i in range(1, m):
    mat[0][i] += mat[0][i - 1]
for i in range(1, n):
    mat[i][0] += mat[i - 1][0]
for i in range(n - 1):
    for j in range(m - 1):
        mat[i + 1][j + 1] = max(mat[i + 1][j], mat[i][j + 1]) + mat[i + 1][j + 1]

print(mat[n - 1][m - 1])






#ASMR?











