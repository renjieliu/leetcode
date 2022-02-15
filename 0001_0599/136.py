class Solution:
    def singleNumber(self, nums: 'List[int]') -> int:
        curr = 0 
        for n in nums: #all the other number will be Xor'ed to 0, as they will appear twice
            curr ^= n
        return curr



# previous approach

# class Solution:
#     def singleNumber(self, nums: 'List[int]') -> int:
#         if len(nums) < 2:
#             return nums[0]
#         else:
#             for i in range(1, len(nums)):
#                 nums[i] = nums[i] ^ nums[i - 1]
#             return nums[-1]

# #         hmp = {}
# #         for n in nums:
# #             if n not in hmp :
# #                 hmp[n] =0
# #             hmp[n] +=1
# #         for k, v in hmp.items():
# #             if v ==1 :
# #                 return k