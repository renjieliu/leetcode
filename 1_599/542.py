class Solution:
    def updateMatrix(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        dp = []
        default = float('inf')
        for r in range(len(matrix)):  # top down
            dp.append([])
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    dp[-1].append(0)
                else:  # need to find 0's, from left, upper, upper right, upper left
                    if r == 0:
                        if c == 0:
                            dp[-1].append(default)
                        else:
                            dp[-1].append(dp[r][c - 1] + 1)
                    else:
                        if c == 0:
                            if len(matrix[0]) == 1:
                                dp[-1].append(dp[r - 1][c] + 1)
                            else:
                                dp[-1].append(min(dp[r - 1][c] + 1, dp[r - 1][c + 1] + 2))
                        elif c == len(matrix[0]) - 1:
                            if len(matrix[0]) == 1:
                                dp[-1].append(dp[r - 1][c])
                            else:
                                dp[-1].append(min(dp[r][c - 1] + 1, dp[r - 1][c - 1] + 2, dp[r - 1][c] + 1))
                        else:
                            dp[-1].append(
                                min(dp[r][c - 1] + 1, dp[r - 1][c] + 1, dp[r - 1][c - 1] + 2, dp[r - 1][c + 1] + 2))

        for r in range(len(matrix) - 1, -1, -1):  # bottom up
            for c in range(len(matrix[0]) - 1, -1, -1):
                if matrix[r][c] == 0:
                    dp[r][c] == 0
                else:
                    if r == len(matrix) - 1:
                        if c == len(matrix[0]) - 1:
                            dp[r][c] = min(dp[r][c], default)
                        else:
                            dp[r][c] = min(dp[r][c], dp[r][c + 1] + 1)
                    else:
                        if c == 0:
                            if len(matrix[0]) == 1:
                                dp[r][c] = min(dp[r][c], dp[r + 1][c] + 1)
                            else:
                                dp[r][c] = min(dp[r][c], dp[r][c + 1] + 1, dp[r + 1][c] + 1, dp[r + 1][c + 1] + 2)
                        elif c == len(matrix[0]) - 1:
                            if len(matrix[0]) == 1:
                                dp[r][c] = min(dp[r][c], dp[r + 1][c] + 1)
                            else:
                                dp[r][c] = min(dp[r][c], dp[r + 1][c - 1] + 2, dp[r + 1][c] + 1)
                        else:
                            dp[r][c] = min(dp[r][c], dp[r][c + 1] + 1, dp[r + 1][c] + 1, dp[r + 1][c + 1] + 2,
                                           dp[r + 1][c - 1] + 2)
        return dp







