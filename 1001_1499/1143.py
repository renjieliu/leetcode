class Solution:
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1))] for _ in range(len(text2))]
        # when start comparing, it's comparing with the "", so the first column and the first row of the matrix should all be 0

        # for r in range(len(dp)):
        #     if r == 0:
        #         for c in range(len(dp[0])):
        #             dp[r][c] =0
        #     dp[r][0] = 0
        # dp matrix has len(text1)+1 cols and len(text2)+1 rows
        for r in range(len(text2)):
            for c in range(len(text1)):
                if text2[r] == text1[c]:
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    if r == 0 and c == 0:
                        dp[r][c] = 0
                    elif r == 0 and c != 0:
                        dp[r][c] = dp[0][c - 1]
                    elif r != 0 and c == 0:
                        dp[r][c] = dp[r - 1][0]
                    else:
                        dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

        return dp[-1][-1]






