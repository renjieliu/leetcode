class Solution:
    def minCostII(self, costs: 'List[List[int]]') -> int:
        def helper(dp, costs, row, color):  # to find the min in the nxt lines, as long as it's not the same color
            if dp[row][color] != float('inf'):  # calculated before
                return dp[row][color]
            else:
                if row == len(costs) - 1:  # if it's last line, simply return the current cost
                    dp[row][color] = costs[row][color]
                    return dp[row][color]
                else:
                    for i in range(len(dp[0])):  # for current, find the min in the following rows
                        if i != color:
                            nxt = helper(dp, costs, row + 1, i)
                            dp[row][color] = min(dp[row][color], costs[row][color] + nxt)
                    return dp[row][color]

        dp = [[float('inf') for _ in range(len(costs[0]))] for _ in range(len(costs))]

        for i in range(len(costs[0])):  # for each one in the first row,find the min in the following rows
            helper(dp, costs, 0, i)
        return min(dp[0])


