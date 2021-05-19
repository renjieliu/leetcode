class Solution:
    def subsetXORSum(self, nums: 'List[int]') -> int:
        curr = 0
        for n in nums:
            curr |=n
        return curr * (2**(len(nums)-1))


# previous approach
# class Solution:
#     def subsetXORSum(self, nums: 'List[int]') -> int:
#         def xor(arr):
#             output = arr[0]
#             for a in arr[1:]:
#                 output^=a
#             return output
#
#         def combo(output, arr, curr, v):
#             if len(curr) == v:
#                 output[0] += xor(curr)
#             else:
#                 for i in range(len(arr)):
#                     combo(output, arr[i+1:], curr + [arr[i]], v)
#         output = [0]
#
#         for i in range(1,len(nums)+1):
#             combo(output, nums, [], i)
#         return output[0]
#
