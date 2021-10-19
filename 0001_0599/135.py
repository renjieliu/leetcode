class Solution:
    def candy(self, ratings: 'List[int]') -> int:
        if len(ratings) == 1:
            return 1
        dp = [None] * len(ratings)

        def helper(dp, ratings, pos):  # this is to find the end of the decreasing slope
            # print(dp)
            if dp[pos] != None:
                return dp[pos]
            else:
                if pos == len(dp) - 1:
                    dp[pos] = 1 if ratings[-1] <= ratings[-2] else (dp[pos - 1] + 1)
                elif pos == 0:
                    if ratings[pos] <= ratings[pos + 1]:
                        dp[pos] = 1
                    else:
                        dp[pos] = 1 + helper(dp, ratings, pos + 1)
                else:  # compare with the neighbours, and get the result.
                    if ratings[pos - 1] < ratings[pos] <= ratings[pos + 1]:
                        dp[pos] = 1 + dp[pos - 1]
                    elif ratings[pos + 1] < ratings[pos] <= ratings[pos - 1]:
                        dp[pos] = 1 + helper(dp, ratings, pos + 1)
                    elif ratings[pos] > ratings[pos + 1] and ratings[pos] > ratings[pos - 1]:
                        dp[pos] = 1 + max(dp[pos - 1], helper(dp, ratings, pos + 1))
                    elif ratings[pos] <= ratings[pos + 1] and ratings[pos] <= ratings[pos - 1]:
                        dp[pos] = 1
                return dp[pos]

        for i in range(len(ratings)):  # find candies for each one.
            helper(dp, ratings, i)
        # print(dp)
        return sum(dp)




