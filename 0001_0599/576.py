class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        dp = [ [{} for c in range(n)] for r in range(m)]
        def helper(dp, m, n, sr, sc, rem): # m is total rows, n is total columns, rem is the moves remaining
            if rem in dp[sr][sc]:
                return dp[sr][sc][rem]
            elif rem == 0:
                return 0
            else:
                dp[sr][sc][rem] = 0
                direction  = [[0,1], [1,0], [-1, 0], [0,-1]]
                for a , b in direction: #check current move and go to next cell,
                    nxt_r = sr + a
                    nxt_c = sc + b
                    if nxt_r < 0 or nxt_r == m or nxt_c < 0 or nxt_c == n:
                        dp[sr][sc][rem] +=1
                    else:
                        dp[sr][sc][rem] += helper(dp, m, n,nxt_r, nxt_c, rem - 1)
                return dp[sr][sc][rem]

        helper(dp, m,n, startRow, startColumn, maxMove)
        # print(dp)
        return dp[startRow][startColumn][maxMove] % (10**9+7)
