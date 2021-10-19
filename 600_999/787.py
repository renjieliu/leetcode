class Solution:
    def findCheapestPrice(self, n: int, flights: 'List[List[int]]', src: int, dst: int, K: int) -> int:
        def dfs(curr, stops, dst, n, dp):
            if curr == dst:
                return 0
            if stops < 0: return float("inf")
            if (curr, stops) in hmp:
                return hmp[(curr, stops)]
            ans = float("inf")
            for neighbor in range(n):
                if dp[curr][neighbor] > 0:
                    ans = min(ans, dfs(neighbor, stops - 1, dst, n, dp) + dp[curr][neighbor])
            hmp[(curr, stops)] = ans
            return ans

        dp = [[0 for _ in range(n)] for _ in range(n)]
        hmp = {}
        for s, d, w in flights:
            dp[s][d] = w

        result = dfs(src, K, dst, n, dp)
        return -1 if result == float("inf") else result