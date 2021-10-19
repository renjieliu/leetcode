class Solution:
    def checkMove(self, board: 'List[List[str]]', rMove: int, cMove: int, color: str) -> bool:
        direction = [[1, -1], [-1, -1], [-1, 1], [1, 1], [1, 0], [0, -1], [-1, 0], [0, 1]]
        for a, b in direction:
            cnt = 1
            c = cMove + a
            r = rMove + b
            lastColor = "X"
            while -1 < r < len(board) and -1 < c < len(board) and board[r][c] != ".":  # valid move
                cnt += 1
                lastColor = board[r][c]
                if lastColor == color:  # meet the same color
                    break
                else:
                    c += a
                    r += b
            # print(lastColor, cnt )

            if cnt >= 3 and lastColor == color:
                return True
        return False




