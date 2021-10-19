class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> int:
        dp = []
        for r in range(len(grid)):
            dp.append([])
            for c in range(len(grid[0])):
                if r == 0:
                    if c == 0:
                        dp[-1].append(grid[r][c])
                    else:
                        dp[-1].append(dp[-1][-1] + grid[r][c])
                else:
                    if c == 0:
                        dp[-1].append(dp[r - 1][c] + grid[r][c])
                    else:
                        dp[-1].append(min(dp[r][c - 1] + grid[r][c], dp[r - 1][c] + grid[r][c]))
        return dp[-1][-1]
