#
# 같은 합이 두개가 있고 그 둘 중에 하나는 fh 와 일치하나 다른 하나는 sh와 일치하지 않는다
# 이를 해결하기 위하여 리스트를 만들고 그 리스트를 이용하여 모든 케이스를 해보아야 한다
#
#
#
#
#
#
#
#




heights = []
hasht = {}

inp = input().split()
for i in range(6):
    heights.append(int(inp[i]))
fh = int(inp[6])
sh = int(inp[7])
sm = 0

check = False

heights.sort(reverse=True)

for i in range(len(heights) - 1):
    for j in range(i + 1, len(heights)):
        hasht.setdefault(heights[i] + heights[j], [])
        hasht[heights[i] + heights[j]].append([i, j])

for i in range(len(heights)):
    if hasht.get(fh - heights[i], None):
        for j in range(len(hasht[fh - heights[i]])):
            l = [0, 1, 2, 3, 4, 5]
            t1 = hasht[fh - heights[i]][j][0]
            t2 = hasht[fh - heights[i]][j][1]

            temp1 = heights[i]
            temp2 = heights[t1]
            temp3 = heights[t2]

            l.pop(i)
            l.pop(t1 - 1)
            l.pop(t2 - 2)

            if sh == heights[l[0]] + heights[l[1]] + heights[l[2]]:
                print(temp1, temp2, temp3, sep=' ', end=' ')
                check = True

                heights.pop(i)
                heights.pop(t1 - 1)
                heights.pop(t2 - 2)
                break

    if check: break

for v in heights:
    print(v, end=' ')