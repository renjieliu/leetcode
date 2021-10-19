class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> None: #constant space
        """
        Do not return anything, modify matrix in-place instead.
        """
        def dfs(grid, sr, sc):
            direction = [[1,0], [-1,0], [0,-1], [0,1]]
            for a , b in direction:
                r = sr+a
                c = sc+b
                while -1 < r < len(grid) and -1 < c < len(grid[0]) and grid[r][c] != 0:
                    grid[r][c] = None #mark it to None, so it will not be visited again in the main fuction
                    r+=a
                    c+=b


        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    dfs(matrix, r, c)

        for r in range(len(matrix)): # mark the ones previously marked as None to 0
            for c in range(len(matrix[0])):
                if matrix[r][c] == None:
                    matrix[r][c] = 0


# previous apparoach: m+n space
# class Solution:
#     def setZeroes(self, matrix: 'List[List[int]]') -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         r_stk = []
#         c_stk = []
#         for r in range(len(matrix)):
#             for c in range(len(matrix[0])):
#                 if matrix[r][c] == 0:
#                     r_stk.append(r)
#                     c_stk.append(c)
#         for a in r_stk:
#             for c in range(len(matrix[0])):
#                 matrix[a][c] = 0
#         for c in c_stk:
#             for r in range(len(matrix)):
#                 matrix[r][c] = 0
#
#
