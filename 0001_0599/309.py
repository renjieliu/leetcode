class Solution:
    def maxProfit(self, prices: 'List[int]') -> int: # O( N | 1 )
        sold, hold, nothing = -float('inf'), -float('inf'), 0 # state: sold, hold, or do nothing
        for p in prices: # assign the state at the same time, to avoid intermediate variables
            sold, hold, nothing = hold + p, max(hold, nothing - p), max(nothing, sold) 
            # sold = hold + p (sell, and pocket the money)
            # hold = money out from doing nothing state.. or keep holding. 
            # hold cannot be from sold, becasue 1 day cooldown
            # nothing = previous doing nothing, and doing nothing again. or previous sold, current still sold 
        return max(sold, nothing) # sold or doing nothing. hold is losing money, will not be considered





# class Solution:
#     def maxProfit(self, prices: 'List[int]') -> int: # O( N | 1 )
#         sold, hold, nothing = -float('inf'), -float('inf'), 0 # state: sold, hold, or do nothing
#         for p in prices: # assign the state at the same time, to avoid intermediate variables
#             sold, hold, nothing = hold + p, max(hold, nothing - p), max(nothing, sold) 
#             # sold = hold + p (sell, and pocket the money)
#             # hold = money out from doing nothing state.. or keep holding. 
#             # nothing = previous doing nothing, and doing nothing again. or previous sold, current still sold 
#         return max(sold, nothing) # sold or doing nothing. hold is losing money, will not be considered




# previous solution


# class Solution:
#     def maxProfit(self, prices: 'List[int]') -> int: # O( N**2 | N )
#         dp = [0] * len(prices)
#         for i in range(len(prices)-1, -1, -1): # buy
#             curr = prices[i]
#             for j in range(i+1, len(prices)): # sell 
#                 if prices[j] > curr:
#                     dp[i] = max(dp[i], prices[j] - curr + (dp[j+2] if j+2 < len(prices) else 0))
#             dp[i] = max(dp[i], 0 if i+1 >= len(prices) else dp[i+1]) #no action from current location 
#         return dp[0]
    


# previous solution

# class Solution:
#     def maxProfit(self, prices: 'List[int]') -> int:
#         dp = [0 for _ in range(len(prices))]
#         for buy in range(len(prices)-1,-1,-1): # assuming buying here
#             A = 0 
#             for sell in range(buy+1, len(prices)): #assuming selling here
#                 profit = prices[sell] - prices[buy] 
#                 A = max(A, profit + (0 if sell + 2 >= len(prices) else dp[sell+2]) )
            
#             B = 0 if buy+1>=len(prices) else dp[buy+1]
            
#             dp[buy] = max(A,B)
        
#         return dp[0]

    


# previous approach
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if prices == []: return 0

#         dp = [0] * len(prices)

#         for curr in range(len(prices) - 1, -1, -1):
#             A = 0
#             for sell in range(curr + 1, len(prices)):
#                 profit = (prices[sell] - prices[curr]) + (0 if sell + 2 >= len(dp) else dp[sell + 2])
#                 A = max(profit, A)

#             B = 0 if curr + 1 >= len(dp) else dp[curr + 1]

#             dp[curr] = max(A, B)

#         return dp[0]

