class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []: return 0

        dp = [0] * len(prices)

        for curr in range(len(prices) - 1, -1, -1):
            A = 0
            for sell in range(curr + 1, len(prices)):
                profit = (prices[sell] - prices[curr]) + (0 if sell + 2 >= len(dp) else dp[sell + 2])
                A = max(profit, A)

            B = 0 if curr + 1 >= len(dp) else dp[curr + 1]

            dp[curr] = max(A, B)

        return dp[0]