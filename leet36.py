# class Solution(object):
#     ROWMAX = 9
#     COLMAX = 9
#     BOXMAX = 3
#
#     def checkDup(self, l):
#         d = {}
#         for i in range(self.ROWMAX):
#             if l[i] == '.': continue
#             n = int(l[i])
#             d.setdefault(n, 0)
#             d[n] += 1
#             if d[n] > 1:
#                 return False
#         # if r:
#         #     for i in range(self.ROWMAX):
#         #         if l[i] == '.': continue
#         #         n = int(l[i])
#         #         d.setdefault(n, 0)
#         #         d[n] += 1
#         #         if d[n] > 1:
#         #             return False
#         # else:
#         #     for i in range(self.COLMAX):
#         #         if l[i] == '.': continue
#         #         n = int(l[i][0])
#         #         d.setdefault(n, 0)
#         #         d[n] += 1
#         #         if d[n] > 1:
#         #             return False
#         return True
#
#     # def checkBoxDup(self, m):
#     #     d = {}
#     #     for i in range(self.BOXMAX):
#     #         for j in range(self.BOXMAX):
#     #             if m[i][j] == '.': continue
#     #             n = int(m[i][j])
#     #             d.setdefault(n, 0)
#     #             d[n] += 1
#     #             if d[n] > 1:
#     #                 return False
#     #     return True
#
#     def isValidSudoku(self, board):
#         # check the row
#         for i in range(0, self.ROWMAX):
#             if not self.checkDup(board[i]):
#                 return False
#         # check the col
#         for j in range(0, self.COLMAX):
#             if not self.checkDup(board[0][j] + board[1][j] + board[2][j] +
#                                    board[3][j] + board[4][j] + board[5][j] +
#                                    board[6][j] + board[7][j] + board[8][j]):
#                 return False
#
#         # check the box
#         for k in range(0, self.ROWMAX, 3):
#             for l in range(0, self.COLMAX, 3):
#                 if not self.checkDup(board[k][l] + board[k][l + 1] + board[k][l + 2] +
#                                         board[k+1][l] + board[k+1][l+1] + board[k+1][l+2] +
#                                         board[k+2][l] + board[k+2][l+1] + board[k+2][l+2]):
#                     return False
#         return True
#
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """

# class Solution(object):
#     ROWMAX = 9
#     COLMAX = 9
#     BOXMAX = 3
#
#     def checkDup(self, l):
#         d = {}
#         for i in range(self.ROWMAX):
#             if l[i] == '.': continue
#             n = int(l[i])
#             d.setdefault(n, 0)
#             d[n] += 1
#             if d[n] > 1:
#                 return False
#         return True
#
#     def isValidSudoku(self, board):
#         for i in range(0, 9):
#             r = i // 3
#             c = (i * 3) % 9
#             if not self.checkDup(board[i]) or \
#                 not self.checkDup(board[0][i] + board[1][i] + board[2][i] +
#                                   board[3][i] + board[4][i] + board[5][i] +
#                                   board[6][i] + board[7][i] + board[8][i]) or \
#             not self.checkDup(board[r][c] + board[r][c + 1] + board[r][c + 2] +
#                               board[r + 1][c] + board[r + 1][c + 1] + board[r + 1][c + 2] +
#                               board[r + 2][c] + board[r + 2][c + 1] + board[r + 2][c + 2]):
#                 return False
#
#         return True



    # # check the row
    # for i in range(0, self.ROWMAX):
    #     if not self.checkDup(board[i]):
    #         return False
    # # check the col
    # for j in range(0, self.COLMAX):
    #     if not self.checkDup(board[0][j] + board[1][j] + board[2][j] +
    #                           board[3][j] + board[4][j] + board[5][j] +
    #                           board[6][j] + board[7][j] + board[8][j]):
    #         return False

    # # check the box
    # for k in range(0, self.ROWMAX, 3):
    #     for l in range(0, self.COLMAX, 3):
    #         if not self.checkDup(board[k][l] + board[k][l + 1] + board[k][l + 2] +
    #                                 board[k+1][l] + board[k+1][l+1] + board[k+1][l+2] +
    #                                 board[k+2][l] + board[k+2][l+1] + board[k+2][l+2]):
    #             return False
    # return True
import collections
class Solution(object):
    ROWMAX = 9
    COLMAX = 9
    BOXMAX = 3

    def checkDup(self, l):
        d = {}
        for i in range(self.ROWMAX):
            if l[i] != '.' and d.setdefault(l[i], 0):
                return False
            d[l[i]] = 1
            # if l[i] != '.':
            #
            #     n = int(l[i])
            #     d.setdefault(n, 1)
            #     d[n] += 1
            #     if d[n] > 1:
            #         return False
        return True

    def isValidSudoku(self, board):
        for i in range(0, 9):
            r = (i // 3) * 3
            c = (i * 3) % 9

            if not self.checkDup(board[i]) or \
                    not self.checkDup(board[0][i] + board[1][i] + board[2][i] +
                                              board[3][i] + board[4][i] + board[5][i] +
                                              board[6][i] + board[7][i] + board[8][i]) or \
                    not self.checkDup(board[r][c:c+3]+ board[r + 1][c:c+3] + board[r + 2][c:c+3]):
                return False

        return True


obj = Solution()
dat = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
#print (dat[0] + 2)
print(obj.isValidSudoku(dat))
