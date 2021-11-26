class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        local = 0
        maxx = -float('inf')
        for i in range(len(nums)): #Kadane's algo
            local = max(local+nums[i], nums[i])
            maxx = max(local, maxx) 
        return maxx
            

# previous approach
# class Solution:
#     def maxSubArray(self, nums: 'List[int]') -> int:
#         output = nums[0]
#         curr = nums[0]
#         for n in nums[1:]:
#             curr = max(n, curr + n)
#             output = max(output, curr)
#         return output

