


#m = 11
#n = 14

# instl = ["MOVE 10",
# "TURN 0",
# "MOVE 2",
# "TURN 0",
# "MOVE 5",
# "TURN 1",
# "MOVE 5",
# "TURN 1",
# "MOVE 2",
# "TURN 1",
# "MOVE 3",
# "TURN 0",
# "TURN 0",
# "MOVE 6"]

# input instruction

dir = 0
#offset -> R, U, L, D 순
offset = [[1, 0], [0, 1], [-1, 0], [0, -1]]
xpos, ypos = 0, 0
instl = [] # instruction list

#input
resp = input().split()
m = int(resp[0])
n = int(resp[1])

for i in range(n):
    instl.append(input())

for i in range(len(instl)):
    inp = instl[i].split()
    if inp[0] == "TURN":
        dir = dir + 1 if inp[1] == '0' else dir - 1
        if dir >= 4 or dir < 0:
            dir %= 4
        # if dir >= 4:
        #     dir = 0
        # elif dir < 0:
        #     dir = 3
    else:
    #elif inp[0] == "MOVE":
        xpos += offset[dir][0] * int(inp[1])
        ypos += offset[dir][1] * int(inp[1])

    if not (0 <= xpos <= m and 0 <= ypos <= m):
        print(-1)
        break
else:
    print(xpos, ypos)


