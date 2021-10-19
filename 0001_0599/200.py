class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> int:
        def dfs(checked, grid, sr, sc):
            if checked[sr][sc] == 1 or grid[sr][sc] == "0":
                return None
            else:
                checked[sr][sc] = 1
                for r in range(sr - 1, -1, -1):
                    if dfs(checked, grid, r, sc) == None:
                        break
                for c in range(sc - 1, -1, -1):
                    if dfs(checked, grid, sr, c) == None:
                        break
                for r in range(sr + 1, len(grid)):
                    if dfs(checked, grid, r, sc) == None:
                        break
                for c in range(sc + 1, len(grid[0])):
                    if dfs(checked, grid, sr, c) == None:
                        break

        checked = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and checked[r][c] == 0:
                    cnt += 1
                    dfs(checked, grid, r, c)
        return cnt
