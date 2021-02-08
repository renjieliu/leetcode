class Solution:
    def findDuplicates(self, nums: 'List[int]') -> 'List[int]':
        output = []
        for n in nums: #use n as the index to check if the same index has been marked
            if nums[abs(n)-1] < 0 : #current number is seen before
                output.append(abs(n))
            else:
                nums[abs(n)-1] *= -1
        return output


# previous approach
# def findDuplicates(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     dict  = {}
#     output = list()
#     for i in nums:
#         if i in dict.keys():
#             output.append(i)
#         else:
#             dict[i] = 0
#     return output
#
# print(findDuplicates([4,3,2,7,8,2,3,1]))
