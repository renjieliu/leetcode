class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> bool:
        def checkCol(board):
            for c in range(len(board[0])):
                hmp = set()
                for r in range(len(board)):
                    if board[r][c] != '.':
                        if board[r][c] in hmp:
                            return False
                        else:
                            hmp.add(board[r][c])
            return True

        def checkRow(board):
            for r in range(len(board)):
                hmp = set()
                for c in range(len(board[0])):
                    if board[r][c] != '.':
                        if board[r][c] in hmp:
                            return False
                        else:
                            hmp.add(board[r][c])
            return True

        def checkSmall9(board):
            for i in range(3):
                for j in range(3):
                    hmp = set()
                    for r in range(3):
                        for c in range(3):
                            curr_r = 3*i+r
                            curr_c = 3*j+c
                            if board[curr_r][curr_c] != '.':
                                if board[curr_r][curr_c] in hmp:
                                    return False
            return True

        return checkSmall9(board) and checkRow(board) and checkCol(board)


# previous approach
# def isValidSudoku(board: 'List[List[str]]'):
#     #1. check rows
#
#     for i in range(9):
#         map = []
#         for j in board[i]:
#             if j not in map and j !=".":
#                 map.append(j)
#             elif j in map:
#                 return False
#
#     #2. check columns
#     for c in range(9):
#         map = []
#         for r in range(9):
#             if board[r][c] not in map and board[r][c] !='.':
#                 map.append(board[r][c])
#             elif board[r][c] in map:
#                 return False
#
#     #3. Check each 3*3 grid
#     cube = []
#     for i in range(3):
#         temp = []
#         for j in range(3):
#             temp.append(board[i][j])
#         cube.append(temp)
#
#     map = []
#
#     for i in range(3):
#         for j in cube[i]:
#             if j not in map and j != ".":
#                 map.append(j)
#             elif j in map:
#                 return False
#
#     cube = []
#     for i in range(3):
#         temp = []
#         for j in range(3,6):
#             temp.append(board[i][j])
#         cube.append(temp)
#
#     map = []
#
#     for i in range(3):
#         for j in cube[i]:
#             if j not in map and j != ".":
#                 map.append(j)
#             elif j in map:
#                 return False
#
#
#     cube = []
#     for i in range(3):
#         temp = []
#         for j in range(6,9):
#             temp.append(board[i][j])
#         cube.append(temp)
#
#     map = []
#
#     for i in range(3):
#         for j in cube[i]:
#             if j not in map and j != ".":
#                 map.append(j)
#             elif j in map:
#                 return False
#
#
#
#
#     cube = []
#     for i in range(3,6):
#         temp = []
#         for j in range(3):
#             temp.append(board[i][j])
#
#         cube.append(temp)
#
#     map = []
#
#     for i in range(3):
#         for j in cube[i]:
#             if j not in map and j != ".":
#                 map.append(j)
#             elif j in map:
#                 return False
#
#
#     cube = []
#     for i in range(3, 6):
#         temp = []
#         for j in range(3,6):
#             temp.append(board[i][j])
#
#         cube.append(temp)
#
#     map = []
#
#     for i in range(3):
#         for j in cube[i]:
#             if j not in map and j != ".":
#                 map.append(j)
#             elif j in map:
#                 return False
#
#
#     cube = []
#     for i in range(3, 6):
#         temp = []
#         for j in range(6,9):
#             temp.append(board[i][j])
#
#         cube.append(temp)
#
#     map = []
#
#     for i in range(3):
#         for j in cube[i]:
#             if j not in map and j != ".":
#                 map.append(j)
#             elif j in map:
#                 return False
#
#
#
#
#
#     cube = []
#     for i in range(6,9):
#         temp = []
#         for j in range(3):
#             temp.append(board[i][j])
#
#         cube.append(temp)
#
#     map = []
#
#     for i in range(3):
#         for j in cube[i]:
#             if j not in map and j != ".":
#                 map.append(j)
#             elif j in map:
#                 return False
#
#
#     cube = []
#     for i in range(6,9):
#         temp = []
#         for j in range(3,6):
#             temp.append(board[i][j])
#
#         cube.append(temp)
#
#     map = []
#
#     for i in range(3):
#         for j in cube[i]:
#             if j not in map and j != ".":
#                 map.append(j)
#             elif j in map:
#                 return False
#
#
#
#     cube = []
#     for i in range(6,9):
#         temp = []
#         for j in range(6,9):
#             temp.append(board[i][j])
#
#         cube.append(temp)
#
#     map = []
#
#     for i in range(3):
#         for j in cube[i]:
#             if j not in map and j != ".":
#                 map.append(j)
#             elif j in map:
#                 return False
#
#
#
#
#
#     return True
#
#
# print(isValidSudoku([
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]))
#
#
#
#
# print(isValidSudoku([
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]))
#
#
# print(isValidSudoku([
#      [".", "8", "7", "6", "5", "4", "3", "2", "1"],
#      ["2", ".", ".", ".", ".", ".", ".", ".", "."],
#      ["3", ".", ".", ".", ".", ".", ".", ".", "."],
#      ["4", ".", ".", ".", ".", ".", ".", ".", "."],
#      ["5", ".", ".", ".", ".", ".", ".", ".", "."],
#      ["6", ".", ".", ".", ".", ".", ".", ".", "."],
#      ["7", ".", ".", ".", ".", ".", ".", ".", "."],
#      ["8", ".", ".", ".", ".", ".", ".", ".", "."],
#      ["9", ".", ".", ".", ".", ".", ".", ".", "."]
# ]))
#
# print(isValidSudoku([[".",".",".","9",".",".",".",".","."],
#                      [".",".",".",".",".",".",".",".","."],
#                      [".",".","3",".",".",".",".",".","1"],
#                      [".",".",".",".",".",".",".",".","."],
#                      ["1",".",".",".",".",".","3",".","."],
#                      [".",".",".",".","2",".","6",".","."],
#                      [".","9",".",".",".",".",".","7","."],
#                      [".",".",".",".",".",".",".",".","."],
#                      ["8",".",".","8",".",".",".",".","."]]))
#
#
# print(isValidSudoku([[".",".",".",".","5",".",".","1","."],
#                      [".","4",".","3",".",".",".",".","."],
#                      [".",".",".",".",".","3",".",".","1"],
#                      ["8",".",".",".",".",".",".","2","."],
#                      [".",".","2",".","7",".",".",".","."],
#                      [".","1","5",".",".",".",".",".","."],
#                      [".",".",".",".",".","2",".",".","."],
#                      [".","2",".","9",".",".",".",".","."],
#                      [".",".","4",".",".",".",".",".","."]]))