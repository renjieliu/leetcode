class Solution:
    def removeBoxes(self, boxes: 'List[int]') -> int:
        n = len(boxes)
        dp = [[[0]*n for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for k in range(n): dp[i][i][k] = (k+1)**2

        for l in range(1, n):
            for i in range(n-l):
                j = i+l
                for k in range(i+1):
                    m = i + 1
                    while m < j+1 and boxes[m] == boxes[i]: m += 1
                    q = m - i - 1
                    ans = (k+q+1)**2 + (dp[m][j][0] if m <= j else 0)
                    for p in range(m, j+1):
                        if boxes[p] == boxes[m-1]: ans = max(ans, dp[m][p-1][0] + dp[p][j][k+q+1])
                    dp[i][j][k] = ans
        return dp[0][n-1][0]

