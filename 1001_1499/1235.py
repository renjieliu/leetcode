import bisect;
class Solution:
    def jobScheduling(self, startTime: 'List[int]', endTime: 'List[int]', profit: 'List[int]') -> int: # RL 20221126: copied solution. O( NlogN | N )
        videos = sorted(list(zip(startTime, endTime, profit)))
        S = [i[0] for i in videos]
        n = len(videos)
        dp = [0] * (n + 1)
        for k in range(n-1, -1, -1):
            temp = bisect_left(S, videos[k][1])
            dp[k] = max(videos[k][2] + dp[temp], dp[k+1])
        return dp[0]

    

# previous solution

# import bisect


# class Solution: #RL 20210828: Copied solution
#     def jobScheduling(self, S, E, profit):
#         videos = sorted(list(zip(S, E, profit)))
#         S = [i[0] for i in videos]
#         n = len(videos)
#         dp = [0] * (n + 1)
#         for k in range(n - 1, -1, -1):
#             temp = bisect_left(S, videos[k][1])
#             dp[k] = max(videos[k][2] + dp[temp], dp[k + 1])
#         return dp[0]


