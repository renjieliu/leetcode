def surfaceArea(grid: 'List[List[int]]'):
    N = len(grid)
    sum = 0
    for i in range(0, N):  # the row
        for j in range(0, N):  # the column
            if i == 0 and j == 0:  # the first grid
                sum += (6*grid[i][j]) - (0 if grid[i][j] ==0 else 2*(grid[i][j]-1))

            else:
                if i == 0 and j != 0:  # first row
                    sum += (6*grid[i][j]) - (0 if grid[i][j] ==0 else 2*(grid[i][j]-1))
                    sum -= 2*(grid[i][j] if grid[i][j] < grid[i][j - 1] else grid[i][j - 1]) # deduct the ones on the prev col
                else:
                    if i != 0 and j == 0:  # first column
                        sum += (6*grid[i][j]) - (0 if grid[i][j] ==0 else 2*(grid[i][j]-1))
                        sum -= 2*(grid[i][j] if grid[i][j] < grid[i - 1][j] else grid[i-1][j]) #deduct the ones on the prev row

                    else:
                        sum += (6*grid[i][j]) - (0 if grid[i][j] ==0 else 2*(grid[i][j]-1))
                        sum -= 2 * (grid[i][j] if grid[i][j] < grid[i - 1][j] else grid[i-1][j])  # deduct the ones on the prev col
                        sum -= 2*(grid[i][j] if grid[i][j] < grid[i][j - 1] else grid[i][j - 1])  # deduct the ones on the prev row

    return sum


print(surfaceArea([[2]]))
print(surfaceArea([[1, 2], [3, 4]])) #34
print(surfaceArea([[1, 0], [0, 2]])) #16
print(surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]])) #32
print(surfaceArea([[2,2, 2], [2, 1, 2], [2, 2, 2]]))  #46
