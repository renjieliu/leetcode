class Solution:
    def minCost(self, costs: 'List[List[int]]') -> int:
        dp = [[float('inf'), float('inf'), float('inf')] for c in costs]
        def dfs(dp, costs, pos, color):
            if dp[pos][color] != float('inf'):
                return dp[pos][color]
            elif pos == len(costs)-1:
                dp[pos][color] = costs[pos][color]
                return dp[pos][color]
            else:
                arr = [[1,2],[0,2], [0,1]] # the color can be picked in the next row
                A = dfs(dp, costs, pos+1, arr[color][0])
                B = dfs(dp, costs, pos+1, arr[color][1])
                dp[pos][color] = costs[pos][color] + min(A, B)
                return dp[pos][color]

        for color in range(3):
            dfs(dp, costs, 0, color)
        return min(dp[0])

# previous approach

# class Solution:
#     def minCost(self, costs: 'List[List[int]]') -> int:
#         if costs == []:
#             return 0
#         dp = [costs[-1]] #
#         i = len(costs)-2
#         while i > -1:#top-down
#             c = costs[i]
#             a = min(c[0] + dp[-1][1], c[0] + dp[-1][2])
#             b = min(c[1] + dp[-1][0], c[1] + dp[-1][2])
#             c = min(c[2] + dp[-1][0], c[2] + dp[-1][1])
#             dp.append([a,b,c])
#             i-=1
#         return min(dp[-1])