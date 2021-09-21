class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> int: #dp: curr to store the local max
        output = 0
        curr = 0 #length of current 1 segment
        for n in nums:
            if n == 1:
                curr += 1
                output = max(output, curr)
            else:
                curr = 0
        return output


# 2 pointers, variable left to record the start loc of 1 in current segment.
#         left = None #loc of first 1 in current segment
#         output = 0
#         for i, n in enumerate(nums):
#             if n == 1:
#                 if left != None:
#                     output = max(output, i-left+1)
#                 else:
#                     left = i
#                     output = max(output, 1)
#             else:
#                 left = None
#         return output


# previous approach
# def findMaxConsecutiveOnes( nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     temp = list()
#     cnt = 0
#     for i in range(0, len(nums)):
#          if nums[i] ==1:
#              cnt += 1
#          else:
#             temp.append(cnt)
#             cnt = 0
#          if i ==  len(nums) -1 :
#              temp.append(cnt)
#     return max(temp)
#
# print(findMaxConsecutiveOnes( [1,1,0,1,1,1]))
#
#
#
#
