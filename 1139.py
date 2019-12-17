class Solution:
    def largest1BorderedSquare(self, grid: 'List[List[int]]') -> int:
        output, X, Y = 0, 0, 0
        dp = []  # put in the continuous 1's on the X and Y axis
        for r in range(len(grid)):
            dp.append([])
            for c in range(len(grid[0])):
                X = Y = 0
                if grid[r][c] == 1:
                    Y = 1 if r == 0 else 1 + dp[r - 1][c][1]
                    X = 1 if c == 0 else 1 + dp[r][c - 1][0]
                    dp[-1].append([X, Y])
                else:
                    dp[-1].append([0, 0])

                candidate = X if X < Y else Y
                while candidate > output:  #
                    if dp[r - candidate + 1][c][0] >= candidate and dp[r][c - candidate + 1][
                        1] >= candidate:  # right upper, lower left of the square
                        output = max(output, candidate)
                        # print (r,c, output ,candidate,  dp )
                        candidate -= 1
                        break
                    candidate -= 1

        return output ** 2