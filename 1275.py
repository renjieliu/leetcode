class Solution:
    def tictactoe(self, moves: 'List[List[int]]') -> str:
        arr = [[None for _ in range(3)] for _ in range(3)]
        for i, (r, c) in enumerate(moves):
            arr[r][c] = "A" if i % 2 == 0 else "B"
        for r in arr:
            if len(set(r)) == 1:
                if r[0] != None:
                    return r[0]
        for c in range(3):
            curr = []
            for r in arr:
                curr.append(r[c])
            if len(set(curr)) == 1:
                if curr[0] != None:
                    return curr[0]
        if arr[0][0] == arr[1][1] == arr[2][2] != None:
            return arr[0][0]
        elif arr[0][-1] == arr[1][1] == arr[2][0] != None:
            return arr[0][-1]
        return "Draw" if len(moves) == 9 else "Pending"




# previous approach
# class Solution:
#     def tictactoe(self, moves: 'List[List[int]]') -> str:
#         win = [[[0, 0], [0, 1], [0, 2]],
#                [[1, 0], [1, 1], [1, 2]],
#                [[2, 0], [2, 1], [2, 2]],
#                [[0, 0], [1, 0], [2, 0]],
#                [[0, 1], [1, 1], [2, 1]],
#                [[0, 2], [1, 2], [2, 2]],
#                [[0, 0], [1, 1], [2, 2]],
#                [[0, 2], [1, 1], [2, 0]]
#                ]
#         i = 0
#         A = []
#         B = []
#         while i < len(moves):
#             if i % 2 == 0:
#                 A.append(moves[i])
#                 if len(A) >= 3:
#                     for w in win:
#                         cnt = 0
#                         for a in w:
#                             if a in A:
#                                 cnt += 1
#                         if cnt == 3:
#                             return "A"
#
#             else:
#                 B.append(moves[i])
#                 if len(B) >= 3:
#                     for w in win:
#                         cnt = 0
#                         for a in w:
#                             if a in B:
#                                 cnt += 1
#                         if cnt == 3:
#                             return "B"
#
#             i += 1
#
#         if len(moves) == 9:
#             return "Draw"
#         else:
#             return "Pending"
