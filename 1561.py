class Solution:
    def maxCoins(self, piles: 'List[int]') -> int:
        output = 0
        piles.sort()
        while piles:
            output += piles[-2] #pick the second largest each time
            piles.pop(0)
            piles.pop()
            piles.pop()

        return output