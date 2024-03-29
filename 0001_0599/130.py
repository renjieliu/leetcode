class Solution:
    def solve(self, board: 'List[List[str]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, r, c): 
            if -1<r<len(board) and -1<c<len(board[0]) and board[r][c] == "O":
                board[r][c] = "E"
                direction = [[1,0], [-1,0], [0,-1], [0,1]]
                for a, b in direction:
                    dfs(board, r+a, c+b)
        
        for c in range(len(board[0])): # just check all the cells connected to the border, and mark them as E
            dfs(board, 0, c)
            dfs(board, len(board)-1, c)
        
        for r in range(len(board)):
            dfs(board, r, 0)
            dfs(board, r, len(board[0])-1)
                
                
        for r in range(len(board)): # mark the cell connect to the border as "O", and others should be "X"
            for c in range(len(board[0])):
                if board[r][c]=="E":
                    board[r][c] = "O"
                else: 
                    board[r][c] = "X"
                    
                    



# previous approach
# class Solution:
#     def solve(self, board: 'List[List[str]]') -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """

#         def dfs(check, sr, sc, board):
#             if board[sr][sc] == 'X' or check[sr][sc] == 1:  # 1 means it has been checked, and it needs flipped
#                 return
#             else:
#                 check[sr][sc] = 1
#                 if sr - 1 > -1:
#                     dfs(check, sr - 1, sc, board)
#                 if sr + 1 < len(board):
#                     dfs(check, sr + 1, sc, board)
#                 if sc - 1 > -1:
#                     dfs(check, sr, sc - 1, board)
#                 if sc + 1 < len(board[0]):
#                     dfs(check, sr, sc + 1, board)

#         if board:
#             check = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
#             for c in range(len(board[0])):  # first row
#                 if board[0][c] == 'O' and check[0][c] == 0:
#                     dfs(check, 0, c, board)
#             for c in range(len(board[0])):  # last row
#                 if board[-1][c] == 'O' and check[-1][c] == 0:
#                     dfs(check, len(board) - 1, c, board)

#             for r in range(len(board)):  # first col
#                 if board[r][0] == 'O' and check[r][0] == 0:
#                     dfs(check, r, 0, board)

#             for r in range(len(board)):  # last col
#                 if board[r][-1] == 'O' and check[r][-1] == 0:
#                     dfs(check, r, len(board[0]) - 1, board)

#                     # print(check)
#             for r in range(len(check)):
#                 for c in range(len(check[0])):
#                     board[r][c] = 'X' if check[r][c] == 0 else 'O'

















