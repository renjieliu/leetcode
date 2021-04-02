class Solution:
    def findMaxForm(self, strs: 'List[str]', m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            zero = s.count("0")
            one = len(s) - zero
            for i in range(m, zero-1, -1): #from total 0 to curr zero count
                for j in range(n, one-1, -1): # from total 1 to curr 1 count to see max previous found "left"
                    dp[i][j] = max(dp[i][j], 1+dp[i-zero][j-one])
        return dp[-1][-1]

