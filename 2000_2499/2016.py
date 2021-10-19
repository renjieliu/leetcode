class Solution:
    def maximumDifference(self, nums: 'List[int]') -> int:
        maxArr = [nums[-1]]  # max number on the right
        for n in nums[::-1][1:-1]:
            maxArr.append(max(n, maxArr[-1]))
        maxArr = maxArr[::-1]
        output = -1
        for i in range(len(nums) - 1):
            if maxArr[i] > nums[i]:
                output = max(output, maxArr[i] - nums[i])
        return output

#         output = -1
#         for i in range(len(nums)):
#             for j in range (i+1, len(nums)):
#                 if nums[j] > nums[i]:
#                     output = max(nums[j] - nums[i], output)
#         return output

