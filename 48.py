class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = 0
        n = len(matrix)
        cnt = 0
        while r <= n // 2:
            c = r
            while c < n - 1 - r:  # only need to pivot to the particular column for the target row.
                curr_r = r
                curr_c = c
                cnt = 0
                curr = matrix[r][c]
                while cnt < 4:  # make 4 changes each time.
                    nxt_r = curr_c
                    nxt_c = n - 1 - curr_r
                    prev = matrix[nxt_r][nxt_c]
                    matrix[nxt_r][nxt_c] = curr
                    curr_r = nxt_r
                    curr_c = nxt_c
                    curr = prev
                    cnt += 1
                c += 1

            r += 1
