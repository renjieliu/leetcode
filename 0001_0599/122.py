class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        output = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]: #greedy to make profit, as long as the price is going up
                output += (prices[i]-prices[i-1])
        return output
 


# previous approach
# class Solution:
#     def maxProfit(self, prices: 'List[int]') -> int:
#         if prices== []:return 0
#         else:
#             output = 0
#             for i in range(1, len(prices)):
#                 if prices[i] - prices[i-1] > 0:
#                     output += (prices[i] - prices[i-1])
#             return output