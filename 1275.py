class Solution:
    def tictactoe(self, moves: 'List[List[int]]') -> str:
        win = [[[0, 0], [0, 1], [0, 2]],
               [[1, 0], [1, 1], [1, 2]],
               [[2, 0], [2, 1], [2, 2]],
               [[0, 0], [1, 0], [2, 0]],
               [[0, 1], [1, 1], [2, 1]],
               [[0, 2], [1, 2], [2, 2]],
               [[0, 0], [1, 1], [2, 2]],
               [[0, 2], [1, 1], [2, 0]]
               ]
        i = 0
        A = []
        B = []
        while i < len(moves):
            if i % 2 == 0:
                A.append(moves[i])
                if len(A) >= 3:
                    for w in win:
                        cnt = 0
                        for a in w:
                            if a in A:
                                cnt += 1
                        if cnt == 3:
                            return "A"

            else:
                B.append(moves[i])
                if len(B) >= 3:
                    for w in win:
                        cnt = 0
                        for a in w:
                            if a in B:
                                cnt += 1
                        if cnt == 3:
                            return "B"

            i += 1

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
