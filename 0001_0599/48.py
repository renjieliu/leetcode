class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> None: # O( MN * 4 | 1 )
        """
        Do not return anything, modify matrix in-place instead.
        """
        total = len(matrix)//2 # total rows to be rotated
        n = len(matrix)-1 # last index of each row
        for r in range(total):
            for c in range(r, n-r):
                prev_r = r 
                prev_c = c 
                prev = matrix[r][c]
                for _ in range(4):
                    nxt_r = prev_c 
                    nxt_c = n - prev_r
                    t = matrix[nxt_r][nxt_c] 
                    matrix[nxt_r][nxt_c] = prev
                    prev_r = nxt_r
                    prev_c = nxt_c
                    prev = t 
                    
                 
        

# previous solution

# class Solution:
#     def rotate(self, matrix: 'List[List[int]]') -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         totalRow = len(matrix) // 2
#         for r in range(totalRow):
#             for c in range(r, len(matrix) - 1 - r):  # no need to fill the last cell of the row.
#                 prev_r = r
#                 prev_c = c
#                 prev_v = matrix[r][c]
#                 for _ in range(4):
#                     rr = prev_c  # the cell to be
#                     rc = (len(matrix) - 1) - prev_r
#                     curr_v = matrix[rr][rc]
#                     matrix[rr][rc] = prev_v
#                     prev_v = curr_v
#                     prev_r = rr
#                     prev_c = rc
#                 # matrix[r][c] = prev_v


# previous solution

# class Solution:
#     def rotate(self, matrix: "List[List[int]]") -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         r = 0
#         n = len(matrix) 
#         cnt = 0
#         while r <= n//2:
#             c = r
#             while c < n-1-r:
#                 curr_r = r 
#                 curr_c = c
#                 cnt = 0 
#                 curr = matrix[r][c]
#                 while cnt < 4:
#                     nxt_r = curr_c
#                     nxt_c = n-1-curr_r
#                     prev = matrix[nxt_r][nxt_c]
#                     matrix[nxt_r][nxt_c] = curr                
#                     curr_r = nxt_r
#                     curr_c = nxt_c
#                     curr = prev
#                     cnt +=1 
#                 c+=1

#             r+=1
        