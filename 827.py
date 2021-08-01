class Solution:
    def largestIsland(self, grid: 'List[List[int]]') -> int:
        def dfs(hmp, grid, sr, sc, slot):  # assign an id to each island
            direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for a, b in direction:
                if -1 < sr + a < len(grid) and -1 < sc + b < len(grid[0]) and grid[sr + a][sc + b] == 1:
                    grid[sr + a][sc + b] = slot
                    dfs(hmp, grid, sr + a, sc + b, slot)

        hmp = {}
        slot = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    slot -= 1
                    grid[r][c] = slot
                    dfs(hmp, grid, r, c, slot)

        for r in range(len(grid)):  # count the size of each island
            for c in range(len(grid[0])):
                slot = grid[r][c]
                if slot != 0:
                    if slot not in hmp:
                        hmp[slot] = 0
                    hmp[slot] += 1

        def lookaround(hmp, grid, sr, sc):  # check neighbours, see what is the size if to connect
            direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            neighbour = []
            for a, b in direction:
                if -1 < sr + a < len(grid) and -1 < sc + b < len(grid[0]):
                    neighbour.append([sr + a, sc + b])
            slots = set()
            for r, c in neighbour:
                if grid[r][c] != 0:
                    slots.add(grid[r][c])
            output = 1
            for s in slots:
                output += hmp[s]
            return output

        output = max(hmp.values()) if hmp else 0

        # print(grid)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                curr = grid[r][c]
                if curr == 0:  # if it's 0, try to connect with neighbours
                    output = max(output, lookaround(hmp, grid, r, c))
        return output

# previous approach
# class Solution(object): # RL 20210801: copied solution
#     def largestIsland(self, grid):
#         N = len(grid)
#
#         def neighbors(r, c):
#             for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
#                 if 0 <= nr < N and 0 <= nc < N:
#                     yield nr, nc
#
#         def dfs(r, c, index):
#             ans = 1
#             grid[r][c] = index
#             for nr, nc in neighbors(r, c):
#                 if grid[nr][nc] == 1:
#                     ans += dfs(nr, nc, index)
#             return ans
#
#         area = {}
#         index = 2
#         for r in range(N):
#             for c in range(N):
#                 if grid[r][c] == 1:
#                     area[index] = dfs(r, c, index)
#                     index += 1
#
#         ans = max(area.values() or [0])
#         for r in range(N):
#             for c in range(N):
#                 if grid[r][c] == 0:
#                     seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
#                     ans = max(ans, 1 + sum(area[i] for i in seen))
#         return ans
#
