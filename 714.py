class Solution:
    def maxProfit(self, prices: 'List[int]', fee: int) -> int:
        cash, balance= 0, -prices[0] #assuming buying the stock on the first day
        for i in range(1, len(prices)):
            cash = max(cash, balance + prices[i]- fee) #sold the stock and get money
            balance = max(balance, cash - prices[i]) # buy the stock again.
        return cash


