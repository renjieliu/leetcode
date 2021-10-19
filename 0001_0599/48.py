class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        totalRow = len(matrix) // 2
        for r in range(totalRow):
            for c in range(r, len(matrix) - 1 - r):  # no need to fill the last cell of the row.
                prev_r = r
                prev_c = c
                prev_v = matrix[r][c]
                for _ in range(4):
                    rr = prev_c  # the cell to be
                    rc = (len(matrix) - 1) - prev_r
                    curr_v = matrix[rr][rc]
                    matrix[rr][rc] = prev_v
                    prev_v = curr_v
                    prev_r = rr
                    prev_c = rc
                # matrix[r][c] = prev_v
