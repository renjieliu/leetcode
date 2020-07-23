class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]': #O(n) and T(1)
        rem = nums[0]
        for n in nums[1:]:  # the result is the ^ of the 2 unique number
            rem ^= n
        diff = rem & (-rem)  # to find the which rightmote bit is different, and divide the numbers to 2 groups.
        output = [0, 0]
        for n in nums:
            if n & diff == 0:  # curr bit diff from the first num
                output[0] ^= n
            else:  # curr bit same as the second number
                output[1] ^= n
        return output



# previous appoache, O(n) and T(n)
# class Solution:
#     def singleNumber(self, nums: List[int]) -> List[int]:
#         hmp = {}
#         for n in nums:
#             if n not in hmp:
#                 hmp[n] = 0
#             hmp[n] += 1
#         output = []
#         for k, v in hmp.items():
#             if v == 1:
#                 output.append(k)
#         return output
