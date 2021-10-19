class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> int:
        dp = []
        for r in range(len(obstacleGrid)):
            dp.append([])
            for c in range(len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 1:
                    dp[-1].append(0)
                else:
                    if r == 0:
                        if c == 0:
                            dp[-1].append(1)
                        else:
                            dp[-1].append(dp[-1][-1])
                    else:
                        if c == 0:
                            dp[-1].append(dp[r-1][0])
                        else:
                            dp[-1].append(dp[r-1][c] + dp[r][c-1])
        return dp[-1][-1]



# previous approach
# def uniquePathsWithObstacles(obstacleGrid: 'List[List[int]]'):
#     output = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
#     for i in range(len(obstacleGrid)): # i row
#         for j in range(len(obstacleGrid[0])): # j col
#             if i==j==0:
#                 if obstacleGrid[i][j] == 1:
#                     return 0
#                 else:
#                     output[i][j]=1
#             elif i==0 and j !=0 :
#                 if obstacleGrid[i][j] == 1 or output[i][j-1] == 0 :
#                     output[i][j] = 0
#                 else:
#                     output[i][j] = 1
#
#             elif i!=0 and j==0 :
#                 if obstacleGrid[i][j] == 1 or output[i-1][j] == 0 :
#                     output[i][j] = 0
#                 else:
#                     output[i][j] =1
#             else:
#                 if obstacleGrid[i][j]==1:
#                     output[i][j] = 0
#
#                 else:
#                     output[i][j] =  output[i-1][j] + output[i][j-1]
#
#     return output[-1][-1]
#
#
# print(uniquePathsWithObstacles([[0,0,0],  [0,1,0],  [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]))
# print(uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))
# print(uniquePathsWithObstacles([[0],[1]]))
# print(uniquePathsWithObstacles([[0,0],[1,0]]))
# print(uniquePathsWithObstacles([[1],[1]]))


