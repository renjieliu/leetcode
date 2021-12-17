class Solution:
    def maximalSquare(self, matrix: 'List[List[str]]') -> int:
        output = 0 
        dp = [[[0,0] for c in range(len(matrix[0])+1)]] # padding one on the top, to avoid "r-1" chaos
        for r in range(len(matrix)):
            dp.append([[0,0]]) # padding one on the top, to avoid "c-1" chaos
            for c in range(len(matrix[0])):
                if matrix[r][c] == "0":
                    dp[-1].append([0,0])
                else:
                    # print(dp, r, c)
                    left = 1 + min(dp[r][c][0], dp[r][c+1][0], dp[r+1][c][0])
                    up = 1 + min(dp[r][c][1], dp[r][c+1][1], dp[r+1][c][1])
                    square = min(left, up)
                    dp[-1].append([square, square])
                output = max(dp[-1][-1][0]**2, output)
        #print(dp)
        return output
	

# previous approach
# class Solution:
#     def maximalSquare(self, matrix: 'List[List[str]]') -> int:
#         dp = []
#         output = 0
#         for r in range(len(matrix)):
#             dp.append([])
#             for c in range(len(matrix[0])):
#                 if r == 0 :
#                     dp[-1].append(int(matrix[r][c]))
#                     output = max(output, dp[-1][-1])
#                 else:
#                     if c==0:
#                         if matrix[r][c] == '1':
#                             dp[-1].append(1)
#                             output = max(output, dp[-1][-1])
#                         else:
#                             dp[-1].append(0)
#                     else:
#                         if matrix[r][c] == '0':
#                             dp[-1].append(0)
#                         else:
#                             dp[-1].append( 1+ min(dp[-1][-1], dp[r-1][c], dp[r-1][c-1]))
#                             output = max(output, dp[-1][-1])
#         return output**2
