class Solution:
    def findKthLargest(self, nums: 'List[int]', k: int) -> int: #O( NlogN | 1 )
        nums.sort()
        return nums[-k]
    

# previous solution

# class Solution:
#     def findKthLargest(self, nums: 'List[int]', k: int) -> int:
#         return sorted(list(nums), reverse = True)[k-1]


# previous solution

# class Solution:
#     def findKthLargest(self, nums: 'List[int]', k: int) -> int:
#         if len(nums)==1:
#             return nums[0]      
        
#         return sorted(nums)[::-1][k-1]



