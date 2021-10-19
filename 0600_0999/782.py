class Solution:
    def movesToChessboard(self, board: 'List[List[int]]') -> int:
        n = len(board)
        patt1 = ([0, 1] * (n // 2 + 1))[:n]
        patt2 = ([1, 0] * (n // 2 + 1))[:n]

        board_t = map(list, zip(*board))
        Cnt_r = list(Counter(tuple(row) for row in board).items())
        Cnt_c = list(Counter(tuple(row) for row in board_t).items())
        if len(Cnt_r) != 2 or len(Cnt_c) != 2: return -1
        if abs(Cnt_r[0][1] - Cnt_r[1][1]) > 1: return -1
        if abs(Cnt_c[0][1] - Cnt_c[1][1]) > 1: return -1

        x1 = sum(i != j for i, j in zip(Cnt_r[0][0], patt1))
        y1 = sum(i != j for i, j in zip(Cnt_c[0][0], patt1))

        x2 = sum(i != j for i, j in zip(Cnt_r[0][0], patt2))
        y2 = sum(i != j for i, j in zip(Cnt_c[0][0], patt2))

        cands_x = [x for x in [x1, x2] if x % 2 == 0]
        cands_y = [y for y in [y1, y2] if y % 2 == 0]

        return min(cands_x) // 2 + min(cands_y) // 2

