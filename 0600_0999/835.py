class Solution:
    def largestOverlap(self, A: 'List[List[int]]', B: 'List[List[int]]') -> int: # RL 20221027 copied solution: O( N**4 | 1 )

        n = len(A)

        def shift_and_count(x_shift, y_shift, M, R):
            """ 
                Shift the matrix M in up-left and up-right directions 
                  and count the ones in the overlapping zone.
                M: matrix to be moved
                R: matrix for reference

                moving one matrix up is equivalent to
                moving the other matrix down
            """
            A, B = 0, 0
            for r_row, m_row in enumerate(range(y_shift, n)): # r_row, r_col is the reference, always starting from 0
                for r_col, m_col in enumerate(range(x_shift, n)):
                    A += (M[m_row][m_col] == R[r_row][r_col] == 1)
                    B += (M[m_row][r_col] == R[r_row][m_col] == 1)

            return max(A, B)

        output = 0
        for r_shift in range(n):
            for c_shift in range(n):
                output = max(output, shift_and_count(r_shift, c_shift, A, B))
                output = max(output, shift_and_count(c_shift, r_shift, B, A))

        return output
    
    



# previous solution

# class Solution:
#     def largestOverlap(self, A: 'List[List[int]]', B: 'List[List[int]]') -> int:
#         def shift(x, y, im1, im2, dim):
#             output = 0
#             for row1, row2 in enumerate(range(y, dim)):
#                 for col1, col2 in enumerate(range(x, dim)):
#                     output += 1 if im1[row1][col1] == 1 and im1[row1][col1] == im2[row2][col2] else 0
#             return output

#         max_overlap = 0

#         for x in range(len(A)):
#             for y in range(len(A)):
#                 max_overlap = max(max_overlap, shift(x, y, A, B, len(A)))
#                 max_overlap = max(max_overlap, shift(x, y, B, A, len(A)))

#         return max_overlap


