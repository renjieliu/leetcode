class Solution:
    def countServers(self, grid: 'List[List[int]]') -> int:
        def dfs(checked, og, sr, sc, cnt):

            checked[sr][sc] = 1
            cnt += 1
            # print(sr,sc, cnt)

            c = sc - 1
            while c > -1:  # go left and check
                if og[sr][c] == 1 and checked[sr][c] == 0:
                    cnt = dfs(checked, og, sr, c, cnt)
                c -= 1

            c = sc + 1
            while c < len(og[0]):  # go right and check
                if og[sr][c] == 1 and checked[sr][c] == 0:
                    cnt = dfs(checked, og, sr, c, cnt)
                c += 1

            r = sr - 1
            while r > -1:  # go up and check
                if og[r][sc] == 1 and checked[r][sc] == 0:
                    cnt = dfs(checked, og, r, sc, cnt)
                r -= 1

            r = sr + 1
            while r < len(og):  # go down and check
                if og[r][sc] == 1 and checked[r][sc] == 0:
                    cnt = dfs(checked, og, r, sc, cnt)
                r += 1

            return cnt  # return how many connected can be found

        og = grid.copy()
        output = 0
        checked = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for r in range(len(og)):
            for c in range(len(og[0])):
                if og[r][c] == 1 and checked[r][c] == 0:
                    cnt = dfs(checked, og, r, c, 0)
                    if cnt > 1:  # it can found more than 1  (the node itself)
                        output += cnt

        return output








