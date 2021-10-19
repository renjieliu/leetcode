class Solution:
    def coinChange(self, coins: 'List[int]', amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for a in range(amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(1+ dp[a-c], dp[a])
        return -1 if dp[-1] == float('inf') else dp[-1]


# previous approach
# def coinChange(coins: 'List[int]', amount: int):
#     if amount ==0 :
#         return 0
#     elif amount < min(coins):
#         return -1
#
#     arr = [float('inf') for _  in range(amount+1)]
#     arr[0] = 0
#     for curr in range(1, len(arr)):
#         for c in coins:
#             if c<=arr[curr] and arr[curr-c] != float('inf'):
#                 arr[curr] = min(arr[curr-c]+1, arr[curr])
#
#     return -1 if arr[amount] == float('inf') else arr[amount]
#
# print(coinChange([1,3,5], 11))



