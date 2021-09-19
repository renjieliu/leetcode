class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        M, N = len(s), len(t)

        # Dynamic Programming table
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)]

        # Base case initialization
        for j in range(N + 1):
            dp[M][j] = 0

        # Base case initialization
        for i in range(M + 1):
            dp[i][N] = 1

        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):

                # Remember, we always need this result
                dp[i][j] = dp[i + 1][j]

                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]





