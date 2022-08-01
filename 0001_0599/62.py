class Solution:
    def uniquePaths(self, m: int, n: int) -> int: #O( MN | MN 
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)] 
        for r in range(m):
            for c in range(n):
                if r == 0:  # only one way to reach, if it's the first row
                    dp[r+1][c+1] = 1 
                elif c == 0: # only one way to reach, if it's the first col
                    dp[r+1][c+1] = 1
                else: # from top + from left
                    dp[r+1][c+1] = dp[r+1][c] + dp[r][c+1]
        return dp[-1][-1]

    
    


# previous solution

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [] 
#         for r in range(m):
#             dp.append([])
#             for c in range(n):
#                 if r == 0:
#                     if c == 0: 
#                         dp[-1].append(1)
#                     else:
#                         dp[-1].append(dp[-1][-1])
#                 else:
#                     if c== 0:
#                         dp[-1].append(dp[r-1][c])
#                     else:
#                         dp[-1].append(dp[r-1][c] + dp[r][c-1])
#         return dp[-1][-1]



# previous approach
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = []
#         for r in range(n):
#             dp.append([])
#             for c in range(m):
#                 if r == 0:
#                     dp[-1].append(1)
#                 else:
#                     if c == 0:
#                         dp[-1].append(1)
#                     else:
#                         dp[-1].append(dp[r][c - 1] + dp[r - 1][c])
#         return dp[-1][-1]



# Previous approach
# def uniquePaths(m: int, n: int):
#     if m*n < 1:
#         return 0
#
#     grid = [[0 for _ in range(n)] for _ in range(m)]
#     for i in range(m): # i : row
#         for j in range(n): # j : col
#             if i ==0 and j ==0:
#                 grid[i][j] = 1
#             elif i==0 or j==0:
#                 grid[i][j] = 1
#
#             else:
#                 grid[i][j] = grid[i-1][j] + grid[i][j-1]
#
#     return grid[-1][-1]
#
#
# print(uniquePaths(3,2))
# print(uniquePaths(7,3))
# print(uniquePaths(3,3))
# print(uniquePaths(1,1))
# print(uniquePaths(0,0))
#
