class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            dp = [1, 1]
            for i in range(2, n + 1):
                curr = 0
                for j in range(1, i + 1):
                    curr += dp[j - 1] * dp[i - j]
                dp.append(curr)
            return dp[-1]




