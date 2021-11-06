class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':
        A = nums[0]
        for n in nums[1:]:
            A^=n
        A = bin(A)[::-1] #to find the first 1 from the right. This is the first differnt bit of the 2 single number
        for i in range(len(A)):
            if A[i] == "1":
                break
        diff = 2**i
        output = [0, 0]
        for n in nums:
            if n & diff == 0: #the bit is not same with the diff 
                output[0] ^= n
            else:
                output[1] ^= n #the bit is same with the diff
        return output
    


# previous approach
# class Solution:
#     def singleNumber(self, nums: 'List[int]') -> 'List[int]': #O(n) and T(1)
#         rem = nums[0]
#         for n in nums[1:]:  # the result is the ^ of the 2 unique number
#             rem ^= n
#         diff = rem & (-rem)  # to find the which rightmote bit is different, and divide the numbers to 2 groups.
#         output = [0, 0]
#         for n in nums:
#             if n & diff == 0:  # curr bit diff from the first num
#                 output[0] ^= n
#             else:  # curr bit same as the second number
#                 output[1] ^= n
#         return output



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
