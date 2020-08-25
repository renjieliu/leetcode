class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> int:
        dp = [0]*(days[-1]+1)
        d_set = set(days)
        for i in range(days[-1] + 1):
            if i not in d_set:
                dp[i] = dp[i-1]
            else:
                day_d = (i-1) if i > 1 else 0
                day_w = (i-7) if i > 7 else 0
                day_m = (i-30) if i > 30 else 0
                dp[i] = min(dp[day_d] + costs[0] , dp[day_w] + costs[1],dp[day_m] + costs[2])
        return dp[-1]