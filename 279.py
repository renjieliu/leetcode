class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
            dp[i] = 1+ min( dp[i-j**2] for j in range(1, int(i**0.5)+1) )
        return dp[n]