class Solution:
    def longestIncreasingPath(self, matrix: 'List[List[int]]') -> int: #O(MN | MN)
        def helper(hmp, grid, r, c): #dfs to find the longest path from here
            if (r, c) in hmp: 
                return hmp[(r,c)]
            else: 
                hmp[(r, c)] = 1
                direction = [[1,0], [0,-1], [-1, 0], [0,1]] #go 4 directions.
                for a, b in direction:
                    nxt_r = r+a
                    nxt_c = c+b
                    if -1 < nxt_r < len(grid) and -1 < nxt_c < len(grid[0]) and grid[nxt_r][nxt_c] > grid[r][c]:
                        hmp[(r, c)] = max(hmp[(r, c)], 1+helper(hmp, grid, nxt_r, nxt_c))
                return hmp[(r,c)]
        
        hmp = {}
        output = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                output = max(output, helper(hmp, matrix, r, c))
        # print(hmp)
        return output
    



# previous solution

# class Solution:
#     def longestIncreasingPath(self, matrix: 'List[List[int]]') -> int:
#         def dfs(dp, grid, sr, sc):
#             if dp[sr][sc] != 0:
#                 return dp[sr][sc]
#             else:
#                 dp[sr][sc] = 1
#                 direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
#                 for d in direction:
#                     r = sr + d[0]
#                     c = sc + d[1]
#                     if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] > grid[sr][sc]:
#                         dp[sr][sc] = max(dp[sr][sc], 1 + dfs(dp, grid, r, c))
#                 return dp[sr][sc]

#         dp = [[0 for c in matrix[0]] for r in matrix]
#         output = 1
#         for r in range(len(matrix)):
#             for c in range(len(matrix[0])):
#                 output = max(output, dfs(dp, matrix, r, c))
#         return output



