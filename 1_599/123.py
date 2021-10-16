class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        A = [0] #from left to right, to check the possible max profit if sell here
        minn = prices[0] 
        for p in prices[1:]:
            A.append(p-minn)
            if p < minn:
                minn = p
        B = [0]
        maxx = prices[-1]
        for p in prices[:-1][::-1]: #from right to left, to check the possible max profit if buy here 
            B.append(maxx - p)
            if p > maxx:
                maxx = p
        
        C = [A[0]]
        for a in A[1:]: # prefix Max of A 
            C.append(max(C[-1], a)) 
        D = B[::-1] # prefix Max of B
        
        
        #print(A, B, C, D)
        
        output = max(max(A), 0) # largest profit if to make transaction only once
        
        for i in range(len(prices)):
            output = max(output, C[i] + (D[i+1] if i+1 < len(prices) else 0 ))
        return output
        
 
        


# previous approach
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices) <= 1:
#             return 0

#         left_min = prices[0]
#         right_max = prices[-1]

#         length = len(prices)
#         left_profits = [0] * length
#         # pad the right DP array with an additional zero for convenience.
#         right_profits = [0] * (length + 1)

#         # construct the bidirectional DP array
#         for l in range(1, length):
#             left_profits[l] = max(left_profits[l-1], prices[l] - left_min)
#             left_min = min(left_min, prices[l])

#             r = length - 1 - l
#             right_profits[r] = max(right_profits[r+1], right_max - prices[r])
#             right_max = max(right_max, prices[r])

#         max_profit = 0
#         for i in range(0, length):
#             max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

#         return max_profit

