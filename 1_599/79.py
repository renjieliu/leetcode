class Solution:
    def exist(self, board: 'List[List[str]]', word: str) -> bool:
        target = list(word)
        def dfs(board, r, c, curr, target, seen):
            if curr == target[0]:
                target.pop(0)
                if target == []:
                    return True
                direction = [[0,1], [1,0], [-1,0], [0,-1]]
                for a , b in direction:
                    if -1 < r+a < len(board) and -1 < c+b < len(board[0]) and (r+a, c+b) not in seen:
                        seen.add((r+a, c+b))
                        if dfs(board, r+a, c+b, board[r+a][c+b], target[:], seen) == 0:
                            seen.remove((r+a, c+b))
                        else:
                            return True
                return False
            else:
                return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==target[0]:
                    seen = {(r, c)}
                    if dfs(board, r, c, board[r][c], target[:], seen):
                        return True
                    seen.remove((r,c))
        return False



# previous approach
# class Solution:
#     def exist(self, board: 'List[List[str]]', word: str) -> bool:
#         def dfs(board, word, r, c, used):
#             if word == "":
#                 return 1
#             else:
#                 for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#                     nxt_r = r + d[0]
#                     nxt_c = c + d[1]
#                     if -1 < nxt_r < len(board) and -1 < nxt_c < len(board[0]) and used[nxt_r][nxt_c] == 0 and \
#                             board[nxt_r][nxt_c] == word[0]:
#                         used[nxt_r][nxt_c] = 1
#                         if dfs(board, word[1:], nxt_r, nxt_c, used) == 1: return 1
#                         used[nxt_r][nxt_c] = 0
#                 return 0
#
#         used = [[0 for c in range(len(board[0]))] for r in range(len(board))]
#         for r in range(len(board)):
#             for c in range(len(board[0])):
#                 if board[r][c] == word[0]:
#                     used[r][c] = 1
#                     if dfs(board, word[1:], r, c, used) == 1:
#                         return 1
#                     used[r][c] = 0
#         return 0

# previous approach
# class Solution:
#     def exist(self, board: 'List[List[str]]', word: str) -> bool:
#         def dfs(word, board, r, c, used, currPath):
#             if word == currPath:
#                 return True
#             elif r >= len(board) or c >= len(board[0]) or r < 0 or c < 0 or used[r][c] == 1:
#                 return False
#             elif board[r][c] != word[len(currPath)]:
#                 return False
#             else:
#                 used[r][c] = 1
#                 if dfs(word, board, r, c - 1, used, currPath + board[r][c]) or dfs(word, board, r, c + 1, used,
#                                                                                    currPath + board[r][c]) or dfs(word,
#                                                                                                                   board,
#                                                                                                                   r - 1,
#                                                                                                                   c,
#                                                                                                                   used,
#                                                                                                                   currPath +
#                                                                                                                   board[
#                                                                                                                       r][
#                                                                                                                       c]) or dfs(
#                         word, board, r + 1, c, used, currPath + board[r][c]):
#                     return True
#                 used[r][c] = 0
#
#         used = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
#         for r in range(len(board)):
#             for c in range(len(board[0])):
#                 if board[r][c] == word[0] and dfs(word, board, r, c, used, "") == True:
#                     return True
#         return False
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
