class Solution:
    def change(self, amount: int, coins: 'List[int]') -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        for r in range(len(dp)):
            for c in range(len(dp[0])):
                if r == 0:
                    dp[r][c] = 1 if c == 0 else 0
                else:
                    if c == 0:
                        dp[r][c] = 1
                    else:
                        # use the current coin + #not using the current coin
                        if c - coins[r - 1] >= 0:
                            dp[r][c] = dp[r][c - coins[r - 1]] + dp[r - 1][c]
                        else:
                            dp[r][c] = dp[r - 1][c]
        return dp[-1][-1]

