class Solution:
    def calculateMinimumHP(self, dungeon: 'List[List[int]]') -> int:
        dp = []
        for r in range(len(dungeon) - 1, -1, -1):  # from right bottom to left upper
            dp.append([])
            for c in range(len(dungeon[0]) - 1, -1, -1):
                if r == len(dungeon) - 1:
                    if c == len(dungeon[0]) - 1:
                        dp[-1].append(0 if dungeon[r][c] >= 0 else dungeon[r][c])
                    else:
                        curr = min(dungeon[r][c] + dp[-1][-1], dungeon[r][c])
                        curr = 0 if curr >= 0 else curr
                        dp[-1].append(curr)
                else:
                    if c == len(dungeon[0]) - 1:  #
                        dp_col = len(dungeon[
                                         0]) - 1 - c  # c is the column of dungeon, the dp column number should be counted from the right
                        curr = min(dungeon[r][c] + dp[-2][dp_col], dungeon[r][c])
                        curr = 0 if curr >= 0 else curr
                        dp[-1].append(curr)
                    else:
                        dp_col = len(dungeon[0]) - 1 - c
                        A = dungeon[r][c] + dp[-2][dp_col]
                        B = dungeon[r][c] + dp[-1][-1]
                        at_least = dungeon[r][c]
                        curr = min(max(A, B), at_least)
                        curr = 0 if curr >= 0 else curr
                        dp[-1].append(curr)
        # print(dp)
        return 1 if dp[-1][-1] >= 0 else abs(dp[-1][-1]) + 1


# previous approach
# class Solution(object):
#     def calculateMinimumHP(self, dungeon):
#         """
#         :type dungeon: List[List[int]]
#         :rtype: int
#         """
#         r, c = len(dungeon), len(dungeon[0])
#         dp = [[float('inf') for i in range(c)] for _ in range(r)]
#
#         def get_min_health(currCell, nextRow, nextCol,r,c):
#             if nextRow >= r or nextCol >= c:
#                 return float('inf')
#             nextCell = dp[nextRow][nextCol]
#             return max(1, nextCell - currCell)
#
#         for row in reversed(range(r)):
#             for col in reversed(range(c)):
#                 currCell = dungeon[row][col]
#
#                 right_health = get_min_health(currCell, row, col+1,r,c)
#                 down_health = get_min_health(currCell, row+1, col,r,c)
#                 curr = min(right_health, down_health)
#
#                 if curr != float('inf'):
#                     min_health = curr
#                 else:
#                     min_health = 1 if currCell >= 0 else (1 - currCell)
#
#                 dp[row][col] = min_health
#
#         return dp[0][0]