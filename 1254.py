class Solution:
    def closedIsland(self, grid: 'List[List[int]]') -> int:
        def dfs(check, sr, sc, grid):
            if check[sr][sc] == 1 or grid[sr][sc] == 1:  # current grid has been checked or no need to proceed
                check[sr][sc] = 1
                return 1
            elif grid[sr][sc] == 0 and (
                    sr == 0 or sr == len(grid) - 1 or sc == 0 or sc == len(grid[0]) - 1):  # 0 is on the border
                # check[sr][sc] =1
                return 2
            elif grid[sr][sc] == 0:
                check[sr][sc] = 1
                border = 0
                for r in range(sr + 1, len(grid)):  # look down
                    t = dfs(check, r, sc, grid)
                    if t == 1:
                        break
                    elif t == 2:
                        border = 1
                        break
                for r in range(sr - 1, -1, -1):  # look up
                    t = dfs(check, r, sc, grid)
                    if t == 1:
                        break
                    elif t == 2:
                        border = 1
                        break
                for c in range(sc - 1, -1, -1):  # look left
                    t = dfs(check, sr, c, grid)
                    if t == 1:
                        break
                    elif t == 2:
                        border = 1
                        break
                for c in range(sc + 1, len(grid[0])):  # look right
                    t = dfs(check, sr, c, grid)
                    if t == 1:
                        break
                    elif t == 2:
                        border = 1
                        break
                if border == 1:
                    return 2
                else:
                    return 3

        check = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if check[r][c] == 0 and grid[r][c] == 0:
                    t = dfs(check, r, c, grid)
                    if t == 3:
                        cnt += 1
        return cnt



























