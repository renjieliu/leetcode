class Solution:
    def getMaximumConsecutive(self, coins: 'List[int]') -> int:
        coins.sort()
        end = 0 #current can reach
        for c in coins:
            if c > end +1: #if current coin is larger than the prev end +1, then the continuous ends.
                return end +1
            else: #the continuous keeps on.
                end += c
        return end+1


