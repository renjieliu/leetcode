def numIslands_dfs(done, grid, sr, sc, output):
    if grid[sr][sc]  == "1":
        grid[sr][sc] = "0"
        done[sr][sc] = 1

        #right
        for c in range(sc+1, len(grid[0])):
            if numIslands_dfs(done, grid, sr, c,output) ==-1:
                break

        # left
        for c in range(sc-1, -1 , -1):
            if numIslands_dfs(done, grid, sr, c,output) == -1:
                break
        # up
        for r in range(sr-1, -1 , -1):
            if numIslands_dfs(done, grid, r, sc,output) == -1:
                break

        # down
        for r in range(sr+1, len(grid)):
            if numIslands_dfs(done, grid, r, sc,output) == -1:
                break

    else:
        return -1


def numIslands(grid: 'List[List[str]]'):
    done = [ [None for _ in range(len(grid[0]))] for _ in range(len(grid)) ]
    output = grid.copy()
    cnt = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if done[r][c] == None and grid[r][c] == "1":
                cnt +=1
                numIslands_dfs(done, grid, r, c, output)

    return cnt

print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(numIslands([["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]]))
print(numIslands([[]]))


