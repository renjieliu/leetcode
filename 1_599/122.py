class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        if prices== []:return 0
        else:
            output = 0
            for i in range(1, len(prices)):
                if prices[i] - prices[i-1] > 0:
                    output += (prices[i] - prices[i-1])
            return output