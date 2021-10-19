class Leaderboard:

    def __init__(self):
        self.board = {}
        self.top_score = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.board:
            self.board[playerId] = 0
        self.board[playerId] += score

        self.top_score = sorted(self.board.values(), reverse=1)  # sort current scores
        # print(self.top_score)

    def top(self, K: int) -> int:
        return sum(self.top_score[:K])

    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0
        self.top_score = sorted(self.board.values(), reverse=1)  # sort current scores

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)





