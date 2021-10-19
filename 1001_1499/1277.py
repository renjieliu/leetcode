class Solution:
    def countSquares(self, matrix: 'List[List[int]]') -> int:
        dp = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        cnt = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0:
                    if matrix[r][c] == 1:
                        dp[r][c] = 1
                        cnt += 1
                    else:
                        dp[r][c] = 0
                else:
                    if c == 0:
                        if matrix[r][c] == 1:
                            cnt += 1
                            dp[r][c] = 1
                        else:
                            dp[r][c] = 0
                    else:
                        if matrix[r][c] == 0:
                            dp[r][c] = 0
                        else:
                            dp[r][c] = min(dp[r - 1][c - 1], dp[r][c - 1], dp[r - 1][c]) + 1
                            cnt += dp[r][c]
        return cnt

# class Solution:
#     def countSquares(self, matrix: 'List[List[int]]') -> int:
#         dp = []
#         output = 0
#         for r in range(len(matrix)):
#             dp.append([])
#             for c in range(len(matrix[0])):  # check the current square length
#                 if r == 0:
#                     if matrix[r][c] == 1:
#                         dp[-1].append(1)
#                     else:
#                         dp[-1].append(0)
#                 elif r > 0:
#                     if matrix[r][c] == 1:
#                         if c == 0:
#                             dp[-1].append(1)
#                         else:
#                             dp[-1].append(1 + min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]))
#                     else:
#                         dp[-1].append(0)
#                 output += dp[-1][-1]  # if c ==3 , it implies it has 2, and 1. so it has 3 submatrix in it
#         return output
#



