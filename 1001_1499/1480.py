class Solution:
    def runningSum(self, nums: 'List[int]') -> 'List[int]': #O(N | N)
        dp = [nums[0]]
        for i in range(1, len(nums)): # accu sum
            dp.append(dp[-1] + nums[i])
        return dp

      


# previous solution

# class Solution:
#     def runningSum(self, nums: 'List[int]') -> 'List[int]':
#         output = [nums.pop(0)]
#         while nums:
#             output.append(output[-1] + nums.pop(0))
#         return output

