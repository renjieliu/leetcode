class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [0] * (n+1)
        def helper(dp, curr): #to drop the egg from curr floor
            if dp[curr] == 0: #it has not been calculated
                for i in range(1, curr+1): #from 1st to curr
                    A = curr if dp[curr] == 0 else dp[curr] # the floor is calculated before
                    B = 1 + max(i-1, helper(dp, curr-i)) #if broke, i-1 to check below floors, if not, helper()to check..
                    dp[curr] = min(A,B)
            return dp[curr]
        helper(dp, n)
        return dp[n]


# previous approach
# class Solution:
#     def twoEggDrop(self, n: int) -> int:
#         #100, 99, 97, 94,90, 85, 79 .... 0 , count how many numbers with this pattern between 0 and n
#         cnt = 0
#         t = 0
#         while n > 0:
#             cnt += 1
#             t += 1
#             n -= t
#         return cnt
