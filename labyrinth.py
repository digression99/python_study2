MX = 10
OFFMAX = 4
#mat = [[0] * 10 for i in range(0, 10)]
mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
offset = [[0, 1], [1, 0], [-1, 0], [0, -1]]
#          x, y

l = []
initx, inity = 1, 1
nowx, nowy = initx, inity

def findPath(l, nx, ny):
    check = False
    for i in range(0, OFFMAX):
        offy, offx = ny + offset[i][0], nx + offset[i][1]

        if mat[offy][offx] == 0:
            check = True
            l.append(offy, offx)
            findPath(l,offx, offy)

    if not check:
        l.pop()
        return

def init(mat):
    for i in range(0, MX):
        for j in range(0, MX):
            if i == 0 or i == MX - 1:
                mat[i][j] = 1
            if j == 0 or j == MX - 1:
                mat[i][j] = 1

#### main ####



#init(mat)
for i in range(0, MX):
    print(mat[i])

l.append((initx, inity))

findPath(mat, l, nowx, nowy)
print(l)
