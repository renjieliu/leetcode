class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1 :
            return k
        elif n == 2:
            return k*k
        else:
            prevprev = k
            prev = k*k
            for i in range(3, n+1):
                curr = (k-1) * prev + (k-1) * prevprev # different from the previous + different from prevprev
                prevprev = prev
                prev = curr
            return curr

# previous approach
# class Solution:
#     def numWays(self, n: int, k: int) -> int:
#         if n == 1:
#             return k
#         dp = [0] * n
#         dp[0] = k
#         dp[1] = k*k
#         for i in range(2, n):
#             dp[i] = (k-1) * dp[i-1] + (k-1)* dp[i-2] # different from the previous and different from curr-2
#         return dp[-1]
