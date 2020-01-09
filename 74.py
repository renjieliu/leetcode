class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        for r in range(len(matrix)):
            if matrix[r][0] == target:
                return True
            elif matrix[r][0] > target:
                if r == 0:
                    return False
                else:
                    for c in range(len(matrix[0])):
                        if matrix[r - 1][c] == target:  # check in the previous row
                            return True
                    return False  # if cannot be found in the previous row, then return false

        if matrix[-1][0] <= target:  # Check last line of the matrix
            for i in matrix[-1]:
                if i == target:
                    return True

        return False
