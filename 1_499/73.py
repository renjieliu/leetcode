class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r_stk = []
        c_stk = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    r_stk.append(r)
                    c_stk.append(c)
        for a in r_stk:
            for c in range(len(matrix[0])):
                matrix[a][c] = 0
        for c in c_stk:
            for r in range(len(matrix)):
                matrix[r][c] = 0


