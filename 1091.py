class Solution:
    def shortestPathBinaryMatrix(self, grid: 'List[List[int]]') -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        elif len(grid) == 1:  # only one element in the grid and it's 0, no need to walk
            return 1
        else:
            arr = [[0, 0]]
            cnt = 1
            while arr:  # BFS to check all the possibilities
                cnt += 1
                nxt = []
                direction = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
                for sr, sc in arr:
                    for x, y in direction:
                        r = sr + x
                        c = sc + y
                        if r == len(grid) - 1 and c == len(grid[0]) - 1 and grid[r][c] == 0:
                            return cnt
                        elif 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
                            nxt.append([r, c])
                            grid[r][c] = 1
                arr = nxt

            return -1






