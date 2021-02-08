def uniquePathsWithObstacles(obstacleGrid: 'List[List[int]]'):
    output = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
    for i in range(len(obstacleGrid)): # i row
        for j in range(len(obstacleGrid[0])): # j col
            if i==j==0:
                if obstacleGrid[i][j] == 1:
                    return 0
                else:
                    output[i][j]=1
            elif i==0 and j !=0 :
                if obstacleGrid[i][j] == 1 or output[i][j-1] == 0 :
                    output[i][j] = 0
                else:
                    output[i][j] = 1

            elif i!=0 and j==0 :
                if obstacleGrid[i][j] == 1 or output[i-1][j] == 0 :
                    output[i][j] = 0
                else:
                    output[i][j] =1
            else:
                if obstacleGrid[i][j]==1:
                    output[i][j] = 0

                else:
                    output[i][j] =  output[i-1][j] + output[i][j-1]

    return output[-1][-1]


print(uniquePathsWithObstacles([[0,0,0],  [0,1,0],  [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]))
print(uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))
print(uniquePathsWithObstacles([[0],[1]]))
print(uniquePathsWithObstacles([[0,0],[1,0]]))
print(uniquePathsWithObstacles([[1],[1]]))


