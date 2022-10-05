class Solution:
    def maxSum(self, grid: 'List[List[int]]') -> int: # O( MN | 1 )
        output = 0
        for r in range(2, len(grid)): # try all the hour glass in the grid, and get the global maximum
            for c in range(2, len(grid[0])):
                output = max(output, grid[r-2][c] + grid[r-2][c-1] + grid[r-2][c-2] + grid[r-1][c-1] + grid[r][c-2] + grid[r][c-1] + grid[r][c]) 
        return output
    



# previous solution

# class Solution:
#     def maxSum(self, grid: 'List[List[int]]') -> int: # O( MN | 1 )
#         output = 0
#         for r in range(2, len(grid)): # try all the hour glass in the grid, and get the global maximum \
#             for c in range(2, len(grid[0])):
#                 output = max(output, grid[r-2][c] + grid[r-2][c-1] + grid[r-2][c-2] + grid[r-1][c-1] + grid[r][c-2] + grid[r][c-1] + grid[r][c]) 
#         return output
    
