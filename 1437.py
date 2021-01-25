class Solution:
    def kLengthApart(self, nums: 'List[int]', k: int) -> bool:
        pre = -k-1
        for i , c in enumerate(nums):
            if c == 1:
                if i - pre -1 < k:
                    return False
                else:
                    pre = i
        return True


#previous approach
# class Solution:
#     def kLengthApart(self, nums: 'List[int]', k: int) -> bool:
#         prev = -float('inf')
#         for i, c in enumerate(nums):
#             if c == 1:
#                 if i - prev > k:
#                     prev = i
#                 else:
#                     return False
#         return True
