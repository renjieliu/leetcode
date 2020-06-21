class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        r, c = len(dungeon), len(dungeon[0])
        dp = [[float('inf') for i in range(c)] for _ in range(r)]

        def get_min_health(currCell, nextRow, nextCol,r,c):
            if nextRow >= r or nextCol >= c:
                return float('inf')
            nextCell = dp[nextRow][nextCol]
            return max(1, nextCell - currCell)

        for row in reversed(range(r)):
            for col in reversed(range(c)):
                currCell = dungeon[row][col]

                right_health = get_min_health(currCell, row, col+1,r,c)
                down_health = get_min_health(currCell, row+1, col,r,c)
                curr = min(right_health, down_health)

                if curr != float('inf'):
                    min_health = curr
                else:
                    min_health = 1 if currCell >= 0 else (1 - currCell)

                dp[row][col] = min_health

        return dp[0][0]