#l = [1, 2, 3, 4, 5]

def test():
    print(l)

offset = [[0, -1], [0, 1], [-1, 0], [1, 0], [1, -1], [-1, 1], [-1, -1], [1, 1]]

def checkCell(grid, i, j):
    cnt = 0

    # for k in range(i - 1, i + 2):
    #     for l in range(j - 1, j + 2):
    #         if 0 <= k < len(grid) and 0 <= l < len(grid[0]) and:
    #             if k != i and l != j:
    #                 if grid[k][l] == 1:
    #                     cnt += 1
    for k in range(8):
        newi = i + offset[k][0]
        newj = j + offset[k][1]
        if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]):
            if grid[newi][newj] == 1:
                 cnt += 1
    return cnt

def evolve(org, rl, cl): # org : original grid, cng : changed grid
    cng = [[0] * rl for i in range(cl)] # changed grid

    for i in range(cl):
        for j in range(rl):
            n = checkCell(org, i, j)
            if org[i][j] == 1:
                if n < 2 or n > 3:
                    cng[i][j] = 0
                else:
                    cng[i][j] = 1
            else:
                if n == 3:
                    cng[i][j] = 1
    return cng



def solve(org, evnum):
    rl = len(org[0]) # row length
    cl = len(org) # col length

    for i in range(evnum):
        org = evolve(org, rl, cl)
        #for j in range(cl):
        #    for k in range(rl):
        #        org[j][k] = l[j][k]
        #        l[j][k] = 0
    cnt = 0

    for i in range(rl):
        for j in range(cl):
            if org[i][j] == 1:
                cnt += 1
    return org

l = [[0, 0, 1],
    [1, 1, 1],
    [1, 1, 1]]

l2 = [[1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1]]

l2 = solve(l2, 1)

print(l2)

l2 = solve(l2, 1)

print(l2)















