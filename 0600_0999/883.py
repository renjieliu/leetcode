def projectionArea(grid: 'List[List[int]]'):
    N = len(grid)
    cnt = 0
    max_row = 0
    max_col = 0
    #1. find all the non empty cell.
    #2. and get the max for each row
    for i in grid:
        max_row = 0
        for j in range(N):
            if i[j]!=0:
                cnt+=1
            if i[j]>max_row:
                max_row = i[j]

        cnt += max_row
    #3. Find the max for each col
    for i in range(N):
        max_col = 0
        for j in range(N):
            if grid[j][i] > max_col :
                max_col = grid[j][i]

        cnt+=max_col

    return cnt

print(projectionArea([[2,2,2],[2,1,2],[2,2,2]]))
print(projectionArea( [[1,1,1],[1,0,1],[1,1,1]]))
print(projectionArea([[1,0],[0,2]]))
print(projectionArea([[1,4],[1,1]]))
