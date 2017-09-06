#xpos, ypos = 0, 0
# map = [[1, 1, 1, 1, 1, 1, 1, 1],
#        [1, 0, 1, 0, 1, 0, 1, 1],
# [1, 0, 1, 0, 0, 0, 0, 1],
# [1, 0, 1, 1, 1, 0, 1, 1],
# [1, 1, 0, 0, 0, 1, 1, 1],
# [1, 0, 0, 1, 0, 1, 1, 1],
# [1, 1, 1, 1, 1, 1, 1, 1]]
#
# map2 = [[1, 1, 0, 0, 0, 1, 1, 1], [0, 1, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 1, 1, 0, 0, 1],
#         [1, 1, 0, 0, 1, 0, 0, 0],
#         [1, 0, 0, 0, 1, 0, 0, 1],
#         [], [], []]




offset = [[-1, 0], [1, 0], [0, -1], [0, 1]]
resp = input().split()
m, n = int(resp[0]), int(resp[1])
mat = [[0] * n for i in range(m)]

for j in range(m):
    s = input()
    for k in range(n):
        mat[j][k] = int(s[k])

def dfs(mat, x, y):
    if y == m - 1:
        return True
    mat[y][x] = 1
    for i in range(4):
        newx = x + offset[i][0]
        newy = y + offset[i][1]
        if (0 <= newx < n and 0 <= newy < m) and mat[newy][newx] == 0:
            if dfs(mat, newx, newy):
                return True
    return False

def solve(mat):
    for i in range(0, n):
        if mat[0][i] == 0:
            if dfs(mat, i, 0):
                return True
    return False

if solve(mat):
    print("YES")
else:
    print("NO")







