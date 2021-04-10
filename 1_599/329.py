class Solution:
    def longestIncreasingPath(self, matrix: 'List[List[int]]') -> int:
        def dfs(dp, grid, sr, sc):
            if dp[sr][sc] != 0:
                return dp[sr][sc]
            else:
                dp[sr][sc] = 1
                direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
                for d in direction:
                    r = sr + d[0]
                    c = sc + d[1]
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] > grid[sr][sc]:
                        dp[sr][sc] = max(dp[sr][sc], 1 + dfs(dp, grid, r, c))
                return dp[sr][sc]

        dp = [[0 for c in matrix[0]] for r in matrix]
        output = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                output = max(output, dfs(dp, matrix, r, c))
        return output



