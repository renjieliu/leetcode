class Solution:
    def beautifulArray(self, n: int) -> 'List[int]':
        dp = {1: [1]}
        def helper(dp, n):
            if n not in dp:
                odds = helper(dp, (n+1)//2)
                evens = helper(dp, n//2)
                dp[n] = [2*x-1 for x in odds] + [2*x for x in evens] # odd (prev*2-1) + even (prev*2)
            #print(n, dp[n])
            return dp[n]

        return helper(dp, n)

# class Solution:
#     def beautifulArray(self, n: int) -> 'List[int]':
#         dp = {1: [1]}
#         def helper(dp, n):
#             if n not in dp:
#                 odds = helper(dp, (n+1)//2)
#                 evens = helper(dp, n//2)
#                 dp[n] = [2*x-1 for x in odds] + [2*x for x in evens] # odd (prev*2-1) + even (prev*2)
#             return dp[n]
#         return helper(dp, n)


