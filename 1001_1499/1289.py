class Solution:
    def minFallingPathSum(self, arr: 'List[List[int]]') -> int:
        if len(arr) == 1:
            return arr[0][0]
        dp = []
        min_dp = []
        for r in range(len(arr)):
            dp.append([])
            min_dp.append(
                [[float('inf'), float('inf')], [float('inf'), float('inf')]])  # initialize the min arr for each row
            for c in range(len(arr[0])):
                if r == 0:
                    dp[-1].append(arr[r][c])
                else:
                    if c == min_dp[r - 1][0][0]:  # the min of the previos is the current column, then add the 2nd min
                        dp[-1].append(arr[r][c] + min_dp[r - 1][1][1])
                    else:
                        dp[-1].append(arr[r][c] + min_dp[r - 1][0][1])

                if dp[r][c] < min_dp[-1][0][1]:  # if it's smaller than the current min,
                    min_dp[-1][1] = min_dp[-1][0].copy()  # keep the the prev min
                    min_dp[-1][0] = [c, dp[r][c]]  # the min of current line
                elif dp[r][c] < min_dp[-1][1][
                    1]:  # greater than the current smallest, but smaller than the 2nd smallest
                    min_dp[-1][1] = [c, dp[r][c]]

        return min_dp[-1][0][1]
