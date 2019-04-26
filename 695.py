def dfs(done, grid, sr, sc, val, currMax):
    if done[sr][sc] == None and grid[sr][sc] == 1:
        done[sr][sc] = 1
        currMax.append(1)
        # up
        for r in range(sr - 1, -1, -1):
            if dfs(done, grid, r, sc, val + 1,  currMax) == -1:
                break

        # down
        for r in range(sr + 1, len(grid)):
            if dfs(done, grid, r, sc, val + 1,  currMax) == -1:
                break
        # left
        for c in range(sc - 1, -1, -1):
            if dfs(done, grid, sr, c, val + 1,  currMax) == -1:
                break

        # right
        for c in range(sc + 1, len(grid[0])):
            if dfs(done, grid, sr, c, val + 1,  currMax) == -1:
                break
    else:
        return -1


def maxAreaOfIsland(grid: 'List[List[int]]'):
    done = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
    res = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if done[r][c] == None and grid[r][c] == 1:
                currMax = []
                dfs(done, grid, r, c, 1, currMax)
                res = max(res, len(currMax))

    return res


print(maxAreaOfIsland(
    [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
