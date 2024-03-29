class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.grid = [[-1 for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        def win(player, r, c, arr):
            good = 1
            for a in arr[r]:  # check row
                if a != player:
                    good = 0
                    break

            if good == 1:
                return player
            good = 1

            for row in arr:  # check col
                if row[c] != player:
                    good = 0
                    break
            if good == 1:
                return player

            good = 1
            for i in range(len(arr)):  # top left to bottom right
                if arr[i][i] != player:
                    good = 0
                    break
            if good == 1:
                return player

            good = 1
            for i in range(len(arr)):  # top right to bottom left
                if arr[i][len(arr) - 1 - i] != player:
                    good = 0
                    break
            if good == 1:
                return player

            return 0

        self.grid[row][col] = player
        return win(player, row, col, self.grid)

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)



# previous approach
# class TicTacToe:
#
#     def __init__(self, n: int):
#         """
#         Initialize your data structure here.
#         """
#         self.dp = [[None for _ in range(n)] for _ in range(n)]
#         self.win = n
#
#     def move(self, row: int, col: int, player: int) -> int:
#         """
#         Player {player} makes a move at ({row}, {col}).
#         @param row The row of the board.
#         @param col The column of the board.
#         @param player The player, can be either 1 or 2.
#         @return The current winning condition, can be either:
#                 0: No one wins.
#                 1: Player 1 wins.
#                 2: Player 2 wins.
#         """
#         self.dp[row][col] = player
#         # print(self.dp)
#         cnt = 0
#         for r in range(self.win):
#             if self.dp[r][col] == player:
#                 cnt += 1
#             else:
#                 break
#         if cnt == self.win:
#             return player
#         else:
#             cnt = 0
#             for c in range(self.win):
#                 if self.dp[row][c] == player:
#                     cnt += 1
#                 else:
#                     break
#             if cnt == self.win:
#                 return player
#             else:
#                 if row != col and row + col != self.win - 1:  # no need to check the diagonal
#                     return 0
#                 else:
#                     cnt = 0
#                     for i in range(self.win):
#                         if self.dp[i][i] == player:
#                             cnt += 1
#                         else:
#                             break
#                     if cnt == self.win:
#                         return player
#                     else:
#                         cnt = 0
#                         for i in range(self.win):
#                             if self.dp[i][-(i + 1)] == player:
#                                 cnt += 1
#                             else:
#                                 break
#                         if cnt == self.win:
#                             return player
#                         else:
#                             return 0
#
# # Your TicTacToe object will be instantiated and called as such:
# # obj = TicTacToe(n)
# # param_1 = obj.move(row,col,player)