class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        r = 0
        while r < len(matrix):
            if matrix[r][0] == target:
                return True
            elif matrix[r][0] > target:
                return False
            else:  # binary search in the current row
                s = 0
                e = len(matrix[0]) - 1
                while s <= e:
                    mid = s - (s - e) // 2
                    if matrix[r][mid] == target:
                        return True
                    elif matrix[r][mid] > target:
                        e = mid - 1
                    else:
                        s = mid + 1
            r += 1
        return False

