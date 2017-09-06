board = [[0] * 10 for i in range(10)]

for j in range(10):
    for k in range(10):
        board[j][k] = j * 2 + k
    print(board[j])

board2 = [board[i][0] for i in range(9)]#lambda col:board[0]
print("\n" + str(board2))

