def numMagicSquaresInside(grid: 'List[List[int]]'):
    if len(grid) < 3 or len(grid[0]) < 3:
        return 0
    else:
        cnt = 0
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                distinct = [grid[r][c], grid[r][c + 1], grid[r][c + 2],
                            grid[r + 1][c], grid[r + 1][c + 1], grid[r + 1][c + 2],
                            grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2]
                            ]
                if sorted(distinct) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    continue

                if grid[r][c] + grid[r][c + 1] + grid[r][c + 2] \
                        == grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2] \
                        == grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2] \
                        == grid[r][c] + grid[r + 1][c] + grid[r + 2][c] \
                        == grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1] \
                        == grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2] \
                        == grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] \
                        == grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c]:
                    cnt += 1

    return cnt


print(numMagicSquaresInside([[4, 3, 8, 4],
                             [9, 5, 1, 9],
                             [2, 7, 6, 2]]))
print(numMagicSquaresInside([[5,5,5],[5,5,5],[5,5,5]]))