class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int: #O( MNK | MNK) K is the maxMove
        def helper(dp, m, n, movesLeft, r, c): #for current location, check how many ways to go out, with movesLeft moves
            if movesLeft in dp[r][c]:
                return dp[r][c][movesLeft]
            else:
                if movesLeft == 0:
                    return 0
                else:
                    dp[r][c][movesLeft] = 0
                    direction = [[-1, 0], [0, -1], [0, 1], [1, 0]] # check the 4 directions
                    for a, b in direction:
                        nxt_r = r+a
                        nxt_c = c+b 
                        if nxt_r == -1 or nxt_c == -1 or nxt_r == m or nxt_c == n:
                            dp[r][c][movesLeft] += 1 
                        else:
                            dp[r][c][movesLeft] += helper(dp, m , n, movesLeft-1, nxt_r, nxt_c)
                    return dp[r][c][movesLeft]
     
        dp = [[{} for _ in range(n)] for _ in range(m)]
        return helper(dp, m, n, maxMove, startRow, startColumn) % (10**9+7)
    
    
    

# previous solution

# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int: # O(MNK | MNK), K is maxMove
#         if maxMove == 0 :
#             return 0
#         dp = [ [{} for c in range(n)] for r in range(m)]
#         def helper(output, dp, m, n, sr, sc, moveLeft): # m is total rows, n is total columns
#             if moveLeft in dp[sr][sc]:
#                 return dp[sr][sc][moveLeft]
#             elif moveLeft == 0:
#                 return 0
#             else:
#                 dp[sr][sc][moveLeft] = 0 
#                 direction  = [[0,1], [1,0], [-1, 0], [0,-1]]
#                 for a , b in direction:
#                     nxt_r = sr + a 
#                     nxt_c = sc + b
#                     if nxt_r < 0 or nxt_r == m or nxt_c < 0 or nxt_c == n:
#                         dp[sr][sc][moveLeft] +=1
#                     else:
#                         dp[sr][sc][moveLeft] += helper(output, dp, m, n,nxt_r, nxt_c, moveLeft - 1)
#                 output[0] += dp[sr][sc][moveLeft]
#                 # print(sr, sc, moveLeft, output)
#                 return dp[sr][sc][moveLeft]
        
#         output = [0]
#         helper(output, dp, m,n, startRow, startColumn, maxMove)
#         # print(dp)
#         return dp[startRow][startColumn][maxMove] % (10**9+7)

                                        
                                        


# previous solution

# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
#         if maxMove == 0:
#             return 0
#         dp = [ [{} for c in range(n)] for r in range(m)]
#         def helper(dp, m, n, sr, sc, rem): # m is total rows, n is total columns, rem is the moves remaining
#             if rem in dp[sr][sc]:
#                 return dp[sr][sc][rem]
#             elif rem == 0:
#                 return 0
#             else:
#                 dp[sr][sc][rem] = 0
#                 direction  = [[0,1], [1,0], [-1, 0], [0,-1]]
#                 for a , b in direction: #check current move and go to next cell,
#                     nxt_r = sr + a
#                     nxt_c = sc + b
#                     if nxt_r < 0 or nxt_r == m or nxt_c < 0 or nxt_c == n:
#                         dp[sr][sc][rem] +=1
#                     else:
#                         dp[sr][sc][rem] += helper(dp, m, n,nxt_r, nxt_c, rem - 1)
#                 return dp[sr][sc][rem]

#         helper(dp, m,n, startRow, startColumn, maxMove)
#         # print(dp)
#         return dp[startRow][startColumn][maxMove] % (10**9+7)
