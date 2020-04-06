class Solution:
    def countSquares(self, matrix: 'List[List[int]]') -> int:
        dp = []
        output = 0
        for r in range(len(matrix)):
            dp.append([])
            for c in range(len(matrix[0])):  # check the current square length
                if r == 0:
                    if matrix[r][c] == 1:
                        dp[-1].append(1)
                    else:
                        dp[-1].append(0)
                elif r > 0:
                    if matrix[r][c] == 1:
                        if c == 0:
                            dp[-1].append(1)
                        else:
                            dp[-1].append(1 + min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]))
                    else:
                        dp[-1].append(0)
                output += dp[-1][-1]  # if c ==3 , it implies it has 2, and 1. so it has 3 submatrix in it
        return output




