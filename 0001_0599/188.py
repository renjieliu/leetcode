class Solution:
    def maxProfit(self, k: int, prices) -> int: # RL 20220910 Copied solution, O( NK | N )
        n = len(prices)

        # solve special cases
        if not prices or k == 0:
            return 0

        # find all consecutively increasing subsequence
        transactions = []
        start = 0
        end = 0
        for i in range(1, n):
            if prices[i] >= prices[i-1]:
                end = i
            else:
                if end > start:
                    transactions.append([start, end])
                start = i
        if end > start:
            transactions.append([start, end])

        while len(transactions) > k:
            # check delete loss
            delete_index = 0
            min_delete_loss = math.inf
            for i in range(len(transactions)):
                t = transactions[i]
                profit_loss = prices[t[1]] - prices[t[0]]
                if profit_loss < min_delete_loss:
                    min_delete_loss = profit_loss
                    delete_index = i

            # check merge loss
            merge_index = 0
            min_merge_loss = math.inf
            for i in range(1, len(transactions)):
                t1 = transactions[i-1]
                t2 = transactions[i]
                profit_loss = prices[t1[1]] - prices[t2[0]]
                if profit_loss < min_merge_loss:
                    min_merge_loss = profit_loss
                    merge_index = i

            # delete or merge
            if min_delete_loss <= min_merge_loss:
                transactions.pop(delete_index)
            else:
                transactions[merge_index - 1][1] = transactions[merge_index][1]
                transactions.pop(merge_index)

        return sum(prices[j]-prices[i] for i, j in transactions)
    
    


# previous solution

# class Solution:
#     def maxProfit(self, k: int, prices) -> int:
#         n = len(prices)

#         # solve special cases
#         if not prices or k == 0:
#             return 0

#         # find all consecutively increasing subsequence
#         transactions = []
#         start = 0
#         end = 0
#         for i in range(1, n):
#             if prices[i] >= prices[i-1]:
#                 end = i
#             else:
#                 if end > start:
#                     transactions.append([start, end])
#                 start = i
#         if end > start:
#             transactions.append([start, end])

#         while len(transactions) > k:
#             # check delete loss
#             delete_index = 0
#             min_delete_loss = math.inf
#             for i in range(len(transactions)):
#                 t = transactions[i]
#                 profit_loss = prices[t[1]] - prices[t[0]]
#                 if profit_loss < min_delete_loss:
#                     min_delete_loss = profit_loss
#                     delete_index = i

#             # check merge loss
#             merge_index = 0
#             min_merge_loss = math.inf
#             for i in range(1, len(transactions)):
#                 t1 = transactions[i-1]
#                 t2 = transactions[i]
#                 profit_loss = prices[t1[1]] - prices[t2[0]]
#                 if profit_loss < min_merge_loss:
#                     min_merge_loss = profit_loss
#                     merge_index = i

#             # delete or merge
#             if min_delete_loss <= min_merge_loss:
#                 transactions.pop(delete_index)
#             else:
#                 transactions[merge_index - 1][1] = transactions[merge_index][1]
#                 transactions.pop(merge_index)

#         return sum(prices[j]-prices[i] for i, j in transactions)



