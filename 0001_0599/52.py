class Solution:
    def totalNQueens(self, n: int) -> int: #O(N! | N ), same approach as N-Queen, just not returning the grid
        def isGood(grid, r, c):
            for _ in range(r): #if same column has Q
                if grid[_][c] == 'Q':
                    return False
            a = r-1
            b = c-1
            while a > -1 and b > -1: #left upper
                if grid[a][b] == 'Q':
                    return False 
                a-=1 
                b-=1 
            
            a = r-1
            b = c+1
            while a > -1  and b < len(grid[0]): # right upper 
                if grid[a][b] == 'Q':
                    return False
                a-=1 
                b+=1 
            return True 
    
        def helper(output, grid, r, curr): #backtracking to try all the possible location.
            if curr == len(grid[0]):
                output[0] += 1
            else:
                for c in range(len(grid[0])): #try for each column
                    grid[r][c] = 'Q'
                    if isGood(grid, r, c):
                        helper(output, grid, r+1, curr+1)
                    grid[r][c] = '.'
        
        grid = [["." for _ in range(n)] for _ in range(n)]
        output = [0]
        helper(output, grid, 0, 0)
        return output[0]
        
        
        


# previous solution

# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         def good(arr, row, col, n):  # if placed current queen at row, col, check if it's valid per previous row setup
#             if arr == []: return 1
#             for r in range(row):
#                 if arr[r][col] == 1:  # check if exists on the same col
#                     return 0
#                 gap = row - r
#                 if row - gap >= 0 and col - gap >= 0 and arr[row - gap][col - gap] == 1:  # check the left above diag
#                     return 0
#                 if row - gap >= 0 and col + gap < n and arr[row - gap][col + gap] == 1:  # check the right above diag
#                     return 0
#             return 1

#         def helper(output, arr, r, c, n, curr):
#             if curr == n:
#                 output.append([])
#                 for r in arr:
#                     output[-1].append("")
#                     for c in r:
#                         output[-1][-1] += ("Q" if c else ".")
#             else:
#                 for r in range(r, n):
#                     for c in range(n):
#                         if good(arr[:r], r, c, n) == 1:  # if it can be placed here
#                             arr[r][c] = 1
#                             helper(output, arr, r + 1, c, n, curr + 1)
#                             arr[r][c] = 0

#         arr = [[0 for _ in range(n)] for _ in range(n)]
#         output = []
#         helper(output, arr, 0, 0, n, 0)
#         return len(output)

