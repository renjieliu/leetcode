def minPathSum(grid: 'List[List[int]]'):
    #bottom up, find the min for each cell
    output = [[0]*len(grid[0])]*len(grid)
    for r in range(len(grid)):
        for c in range(len(grid[0])):

            if r== 0 and c==0:
                output[r][c] = grid[r][c]

            elif r==0 and c != 0 :
                output[r][c] = output[r][c-1] + grid[r][c]

            elif r!=0 and c==0:
                output[r][c] = output[r-1][c] + grid[r][c]
            else:
                output[r][c] = min(output[r-1][c], output[r][c-1]) + grid[r][c]
                print('r','c', r,c , output)

    return output[-1][-1]

print(minPathSum([[1,3,1],
                  [1,5,1],
                  [4,2,1]]))


