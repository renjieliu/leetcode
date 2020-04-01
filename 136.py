class Solution:
    def singleNumber(self, nums: 'List[int]') -> int:
        if len(nums) < 2: return nums[0]
        else:
            curr = nums[0]
            for i in range(1, len(nums)):
                curr =curr^nums[i]
            return curr





# def singleNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     dict = {}
#
#     for i in nums:
#         if i not in dict:
#             dict[i] = 1
#         else:
#             dict[i] += 1
#
#     for k, v in dict.items():
#         if v != 2:
#             return k
#
