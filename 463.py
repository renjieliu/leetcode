def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    sum = 0
    for i in range(0, len(grid)): # i is line, j is row
        for j in range(0, len(grid[i])):
            sum+=grid[i][j]*4
            if i>0 and grid[i-1][j]==1 and grid[i][j] ==1:
                sum-=2
            if j>0 and grid[i][j-1]==1 and grid[i][j] ==1:
                sum-=2

    return sum




print(islandPerimeter([[0,1,0,0],
                       [1,1,1,0],
                       [0,1,0,0],
                       [1,1,0,0]]
                    ))
