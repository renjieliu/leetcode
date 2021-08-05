class Solution:
    def stoneGame(self, piles: 'List[int]') -> bool:
        dp = [[None for _ in range(len(piles))] for _ in range(len(piles))]
        def helper(dp, piles, l, r): #to check how many points Lee can take, if curr boundary is l, r
            if dp[l][r] != None:
                return dp[l][r]
            else:
                if l == r:
                    dp[l][r] = piles[l]
                elif l > r:
                    return 0
                else:
                    dp[l][r] = max(piles[l] - helper(dp, piles, l+1, r)
                                   , piles[r] - helper(dp, piles, l, r-1))

                return dp[l][r]

        helper(dp, piles, 0, len(piles)-1 )
        for r in dp:
            for c in r:
                if c > 0:
                    return True
        return False


# previous approach
# class Solution:
#     def stoneGame(self, piles: 'List[int]') -> bool:
#         dp = [[None for _ in range(len(piles))] for _ in range(len(piles))]
#
#         def points(piles, l, r, dp):
#             if dp[l][r] != None:
#                 return dp[l][r]
#             elif l == r:
#                 dp[l][r] = piles[r]
#                 return dp[l][r]
#             elif l > r:
#                 return 0
#             else:
#                 dp[l][r] = max(piles[l] - points(piles, l + 1, r, dp),
#                                piles[r] - points(piles, l, r - 1, dp)
#                                )
#                 return dp[l][r]
#
#         points(piles, 0, len(piles) - 1, dp)
#
#         for r in dp:
#             for c in r:
#                 if c > 0:
#                     return True
#         return False
