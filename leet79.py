class Solution(object):
    def __init__(self):
        self.offset = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def check(self, board, i, j, u):
        if len(self.word) == u:
            return True

        for k in range(4):
            newi = i + self.offset[k][1]
            newj = j + self.offset[k][0]
            if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                if board[newi][newj] == self.word[u] and self.check(board, newi, newj, u + 1):
                    return True
        return False

    def exist(self, board, word):
        self.word = word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = ''
                    #board[i].pop(j)
                    #board[i].insert(j, '')

                    if self.check(board, i, j, 1):
                        return True
        return False

mat = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']]
mat2 = [['a', 'a']]
word = "ABCCED"
word2 = "SEE"
word3 = "ABCB"
word4 = "aaa"

print(Solution().exist(mat2, word4))
#l = ['a', 'b', 'c', 'd']
#l.pop(3)
#l.insert(3, '')
#print(l)

