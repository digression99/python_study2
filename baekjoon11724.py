inp = list(map(int, input().split()))
n, m = inp[0], inp[1]

setlist = []

for i in range(m):
    inp = list(map(int, input().split())) # inp[0], inp[1]
    v1, v2 = -1, -1 # union

    for j in range(len(setlist)):
        if inp[0] in setlist[j]:
            v1 = j
        if inp[1] in setlist[j]:
            v2 = j
    # x x
    if v1 == -1 and v2 == -1:
        setlist.append({inp[0], inp[1]})
    # o x
    elif v2 == -1:
        setlist[v1].add(inp[1])
    # x o
    elif v1 == -1:
        setlist[v2].add(inp[0])
    # o o
    else:
        if v1 != v2:
            t = 0
            if len(setlist[v1]) > len(setlist[v2]):
                t = v2
                setlist[v1].union(setlist[v2])
            else:
                t = v1
                setlist[v2].union(setlist[v1])
            setlist.pop(t)
print(len(setlist))






    #array[inp[0]].append(inp[1])
    #array[inp[1]].append(inp[0])


# visited = [False] * 1001 # traversal check
# array = [[] for i in range(1001)] # adjacency list
# num = 0
#
# def dfs(visited, start):
#     visited[start] = True
#     for i in range(len(array[start])):
#         if not visited[array[start][i]]:
#             dfs(visited, array[start][i])
#
# for j in range(1, n + 1):
#     if not visited[j]:
#         num += 1
#         dfs(visited, j)
# print(num)

# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6






    #if not inp[0] in

    #idxdict.setdefault(inp[0], 0)






