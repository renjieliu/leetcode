class Solution:
    def countNegatives(self, grid: 'List[List[int]]') -> int:
        r = len(grid) - 1
        cnt = 0
        while r > -1:
            if grid[r][-1] >= 0:
                return cnt
            c = len(grid[0]) - 1
            while c > -1:
                if grid[r][c] < 0:
                    cnt += 1
                else:
                    break
                c -= 1
            r -= 1
        return cnt
