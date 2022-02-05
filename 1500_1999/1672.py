class Solution:
    def maximumWealth(self, accounts: 'List[List[int]]') -> int:
        return max(sum(r) for r in accounts)
    

# previous approach

# class Solution:
#     def maximumWealth(self, accounts: 'List[List[int]]') -> int:
#         return max([sum(a) for a in accounts])


