class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: 'List[List[int]]') -> int:
        grid = [[1 for _ in range(n)] for _ in range(n)]
        for r, c in mines:
            grid[r][c] = 0
        dp = []
        for r in range(n): #from lefttop to rightbottom
            dp.append([])
            for c in range(n):
                if grid[r][c] == 0:
                    dp[-1].append([0,0,0,0])
                else:
                    if r == 0:
                        if c == 0:
                            dp[-1].append([1,1,1,1]) #[left, up, right, down]
                        else:
                            dp[-1].append([dp[-1][-1][0]+1,1,1,1])
                    else:
                        if c==0:
                            dp[-1].append([1, dp[r-1][c][1]+1, 1, 1])
                        else:
                            dp[-1].append([dp[r][c-1][0] +1, dp[r-1][c][1]+1, 1, 1])
        output = -float('inf')
        for r in range(n-1, -1, -1): # from right bottom to left top
            for c in range(n-1, -1, -1):
                if grid[r][c] == 1:
                    if r == n-1:
                        if c == n-1:
                            dp[r][c][2] = 1
                            dp[r][c][3] = 1
                        else:
                            dp[r][c][2] = dp[r][c+1][2] + 1
                    else:
                        if c == n-1:
                            dp[r][c][3] = dp[r+1][c][3] + 1

                        else:
                            dp[r][c][2] = dp[r][c+1][2] +1
                            dp[r][c][3] = dp[r+1][c][3] + 1

                    output = max(output, min(dp[r][c])) # the plus sign is the shortest of 4 directions

        return output if output != -float('inf') else 0












