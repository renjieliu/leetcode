class Solution:
    def maxKilledEnemies(self, grid: 'List[List[str]]') -> int:
        if grid == []: return 0
        output = 0
        dp = [[[0, 0] for _ in range(len(grid[0]))] for _ in
              range(len(grid))]  # each cell is the count from [row and col]
        for r in range(len(grid)):  # for left to right
            e_left_cnt = 0
            for c in range(len(grid[0])):
                if grid[r][c] == 'W':
                    e_left_cnt = 0
                elif grid[r][c] == 'E':
                    e_left_cnt += 1
                else:
                    dp[r][c][0] += e_left_cnt
        for r in range(len(grid)):  # for right to right
            e_right_cnt = 0
            for c in range(len(grid[0]) - 1, -1, -1):
                if grid[r][c] == 'W':
                    e_right_cnt = 0
                elif grid[r][c] == 'E':
                    e_right_cnt += 1
                else:
                    dp[r][c][0] += e_right_cnt
        for c in range(len(grid[0])):
            e_above_cnt = 0
            for r in range(len(grid)):  # top to bottom
                if grid[r][c] == 'W':
                    e_above_cnt = 0
                elif grid[r][c] == 'E':
                    e_above_cnt += 1
                else:
                    dp[r][c][1] += e_above_cnt
        for c in range(len(grid[0])):
            e_below_cnt = 0
            for r in range(len(grid) - 1, -1, -1):  # bottom to top
                if grid[r][c] == 'W':
                    e_below_cnt = 0
                elif grid[r][c] == 'E':
                    e_below_cnt += 1
                else:
                    dp[r][c][1] += e_below_cnt
                    output = max(output, sum(dp[r][c]))

        return output