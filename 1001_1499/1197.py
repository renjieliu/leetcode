class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == y == 0:
            return 0
        stk = [[0, 0]]
        move = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, -2], [-1, 2], [-2, -1], [-2, 1]]
        lkp = {(0, 0)}
        cnt = 0
        while True:
            nxt = []
            cnt += 1
            while stk:
                curr = stk.pop(0)
                for a, b in move:
                    r = curr[0] + a
                    c = curr[1] + b
                    if r == x and c == y:
                        return cnt
                    if (r, c) not in lkp:
                        nxt.append([r, c])
                        lkp.add((r, c))
            stk = nxt

