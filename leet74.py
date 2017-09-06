class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        # binary search
        coll, colh, rowl, rowh = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        if colh < 0 or rowh < 0: return False
        while coll <= colh:
            cmid = (coll + colh) // 2
            if matrix[cmid][0] <= target <= matrix[cmid][rowh]:
                while rowl <= rowh:
                    rmid = (rowl + rowh) // 2
                    if matrix[cmid][rmid] == target:
                        return True
                    elif matrix[cmid][rmid] < target <= matrix[cmid][rowh]:
                        rowl = rmid + 1
                    elif matrix[cmid][rmid] > target >= matrix[cmid][0]:
                        rowh = rmid - 1
                    else:
                        return False
            elif matrix[coll][0] <= target < matrix[cmid][0]:
                colh = cmid - 1
            elif matrix[cmid][rowh] < target <= matrix[colh][rowh]:
                coll = cmid + 1
            else:
                break
        return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """


mat = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
mat2 = [[1]]
mat3 = [[1, 3]]
mat4 = [[1], [3]]
mat5 = [[1, 3, 5]]
tgt = 2

obj = Solution()
print(obj.searchMatrix(mat5, tgt))