class Solution(object):
    def numDecodings(self, S):
        mod, dp = 10**9 + 7, [1, 0, 0]
        for c in S:
            dp_new = [0,0,0]
            if c == '*':
                dp_new[0] = 9*dp[0] + 9*dp[1] + 6*dp[2]
                dp_new[1] = dp[0]
                dp_new[2] = dp[0]
            else:
                dp_new[0]  = (c > '0') * dp[0] + dp[1] + (c <= '6') * dp[2]
                dp_new[1]  = (c == '1') * dp[0]
                dp_new[2]  = (c == '2') * dp[0]
            dp = [i % mod for i in dp_new]
        return dp[0]


