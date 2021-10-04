class Solution:
    def islandPerimeter(self, grid: 'List[List[int]]') -> int:
        total = 0
        for r in range(len(grid)): # for each cell, if the above or left is 1, minus total Length - 2.
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    total += 4
                    if r == 0:
                        if c > 0 and grid[r][c-1] == 1:
                            total -= 2
                    else:
                        if r > 0 and grid[r-1][c] == 1 :
                            total -= 2
                        if c > 0 and grid[r][c-1] == 1:
                            total -=2
        return total


# previous approach
# class Solution:
#     def islandPerimeter(self, grid: 'List[List[int]]') -> int:
#         deduction = 0
#         total = 0
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == 1:
#                     total += 4
#                     if r == 0:
#                         if c > 0 and grid[r][c - 1] == 1:  # prev col
#                             deduction += 2  # 2 edges are elimiated
#                     else:
#                         if grid[r - 1][c] == 1:  # prev row
#                             deduction += 2
#                         if c > 0 and grid[r][c - 1] == 1:  # prev col
#                             deduction += 2
#         return total - deduction
#
