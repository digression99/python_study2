class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        row, col = 0, 0



        while row <= n // 2 and col <= m // 2:
            if row == n // 2 or col == m // 2:
                #if n % 2 == 1 and m % 2 == 1:
                #    ans.append(matrix[row][col])
                #    break
                if n // 2 - row == 0 and n % 2 == 1:
                    for i in range(col, m - col):
                        ans.append(matrix[i][n - 1 - row])
                elif m // 2 - col == 0 and m % 2 == 1:
                    for i in range(row, n - row):
                        ans.append(matrix[m - 1 - col][i])
                break
            for i in range(row, n - 1 - row):
                ans.append(matrix[col][i])
            for j in range(col, m - 1 - col):
                ans.append(matrix[j][n - 1 - row])
            for k in range(n - 1 - row, row, -1):
                ans.append(matrix[m - 1 - col][k])
            for l in range(m - 1 - col, col, -1):
                ans.append(matrix[l][row])
            row += 1
            col += 1
        return ans



# class Solution(object):
#     def spiralOrder(self, matrix):
#         if not matrix:
#             return []
#         m = len(matrix)
#         n = len(matrix[0])
#         ans = []
#         i = 0
#
#         if m == 1 or n == 1:
#             return matrix
#
#         while i <= n // 2:
#             if i == n // 2 and n % 2 == 1:
#                 ans.append(matrix[i][i])
#                 break
#
#             for j in range(i, n - 1 - i):
#                 ans.append(matrix[i][j])
#             for j in range(i, m - 1 - i):
#                 ans.append(matrix[j][n - 1 - i])
#             for j in range(n - 1 - i, i, - 1):
#                 ans.append(matrix[m - 1 - i][j])
#             for j in range(m - 1 - i, i, - 1):
#                 ans.append(matrix[j][i])
#             i += 1
#         return ans

obj = Solution()
testl1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
testl2 = [[1, 2], [3, 4], [5, 6]]
testl3 = [[6, 9, 7]]
testl4 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
testl5 = [[1]]
testl6 = [[2, 3]]
print(obj.spiralOrder(testl1))




#
# int * spiralOrder(int ** matrix, int
# matrixRowSize, int
# matrixColSize) {
#     int * ans = (int *)
# calloc(matrixRowSize * matrixColSize, sizeof(int));
# int
# m = matrixColSize, n = matrixRowSize;
# int
# i = 0, j = 0, idx = 0;
#
# while (i <= n / 2)
#     {
#     if (i == n / 2 & & n % 2 == 1)
#     {
#         ans[idx] = matrix[i][i];
#     break;
#     }
#     for (j = i; j < n - 1 - i; j++)
#     ans[idx++] = matrix[i][j];
#     for (j = i; j < m - 1 - i; ++j)
#     ans[idx++] = matrix[j][n - 1 - i];
#     for (j = n - 1 - i; j > i; --j)
#     ans[idx++] = matrix[m - 1 - i][j];
#     for (j = m - 1 - i; j > i; --j)
#     ans[idx++] = matrix[j][i];
#     ++i;
#     }
# return ans;
# }