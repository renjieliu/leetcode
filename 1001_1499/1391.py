class Solution:
    def hasValidPath(self, grid: 'List[List[int]]') -> bool:
        # 1:R, 2:L, 3: U, 4: D, from current can move 2 directions, and the receiving styles.
        valid = {1: {1: [1, 3, 5], 2: [1, 4, 6]}, \
                 2: {3: [2, 3, 4], 4: [2, 5, 6]}, \
                 3: {2: [1, 4, 6], 4: [2, 5, 6]}, \
                 4: {1: [1, 3, 5], 4: [2, 5, 6]}, \
                 5: {2: [1, 4, 6], 3: [2, 3, 4]}, \
                 6: {1: [1, 3, 5], 3: [2, 3, 4]}}
        direction = [[0, 1, 1], [0, -1, 2], [-1, 0, 3], [1, 0, 4]]  # 1:R, 2:L, 3: U, 4: D
        stk = [[0, 0, grid[0][0]]]  # pos, style, nxt
        sr = sc = 0
        seen = {(0, 0)}
        while stk:
            nxt = []
            while stk:
                sr, sc, style = stk.pop(0)
                if sr == len(grid) - 1 and sc == len(grid[0]) - 1:  # it has reached the last cell
                    return True
                # print(sr, sc)
                for a, b, move in direction:
                    if -1 < sr + a < len(grid) and -1 < sc + b < len(grid[0]) and move in valid[style] and grid[sr + a][
                        sc + b] in valid[style][move]:
                        if (sr + a, sc + b) not in seen:
                            seen.add((sr + a, sc + b))
                            nxt.append([sr + a, sc + b, grid[sr + a][sc + b]])
            stk = nxt
        return sr == len(grid) - 1 and sc == len(grid[0]) - 1  # in the end, to check if it stops at last cell


