class Solution:
    def finalPrices(self, prices: 'List[int]') -> 'List[int]':
        def nextMin(t, arr):
            for a in arr:
                if a <= t:
                    return a
            return 0
        output = []
        for i in range(len(prices)):
            output.append(prices[i] - nextMin(prices[i], prices[i+1:]))
        return output