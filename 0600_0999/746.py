class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> int: # O( N | 1 )
        if len(cost) == 2:
            return min(cost[0], cost[1]) 
        else:
            prev_a = cost[-1]
            prev_b = cost[-2]
            for n in cost[:-2][::-1]: 
                curr  = n + min(prev_a, prev_b)   #the min to reach end from here.
                prev_a = prev_b # prev b to a 
                prev_b = curr # c to prev b
            return min(prev_a, prev_b)
        



# previous solution

# class Solution:
#     def minCostClimbingStairs(self, cost: 'List[int]') -> int:
#         if len(cost) <= 2 :
#             return min(cost[0], cost[-1])
#         else:
#             a = cost[0] #from 0
#             b = cost[1] #from 1
#             for i in range(2, len(cost)):
#                 curr = cost[i] + min(a, b) # current is from a or b + currCost
#                 a = b
#                 b = curr
#             return min(a, b) # min(curr-1, curr-2) + curr


# previous approach
# class Solution:
#     def minCostClimbingStairs(self, cost: 'List[int]') -> int:
#         def dfs(dp, pos, cost):
#             if pos in dp:
#                 return dp[pos]
#             elif pos >= len(cost):
#                 return 0
#             else:
#                 dp[pos] = cost[pos]
#                 A = dfs(dp, pos+1, cost)
#                 B = dfs(dp, pos+2, cost)
#                 dp[pos] += min(A, B)
#                 return dp[pos]
#
#         dp = {}
#         dfs(dp, 0, cost)
#         return min(dp[0], dp[1])

