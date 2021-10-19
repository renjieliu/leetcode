class Solution:
    def reconstructMatrix(upper: int, lower: int, colsum: 'List[int]') -> 'List[List[int]]':
        trouble = []  # the one cannot be immediately decided
        dp = [[0 for _ in range(len(colsum))] for _ in range(2)]
        up = 0
        down = 0
        for c in range(len(colsum)):
            if colsum[c] == 2:
                dp[0][c] = 1
                dp[1][c] = 1
                up += 1
                down += 1
            elif colsum[c] == 1:  # add all the 1's to the upper, this will be adjusted later on.
                dp[0][c] = 1
                dp[1][c] = 0
                up += 1
                trouble.append(c)
        if up + down != sum(
                colsum) or up < upper:  # it cannot be matched anyway, or the current up is already less than the upper
            return []
        else:
            takeOut = up - upper  # how many need to be taken out from the up , and put to the down
            if takeOut > len(trouble):
                return []

            elif lower != down + takeOut:
                return []

            else:
                for t in range(takeOut):  # shift the up to the down
                    x = trouble.pop(0)
                    dp[0][x] = 0
                    dp[1][x] = 1

        return dp