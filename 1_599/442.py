class Solution:
    def findDuplicates(self, nums: 'List[int]') -> 'List[int]':
        output = []
        for n in nums:
            pos = abs(n)-1 
            if nums[pos] > 0:
                nums[pos] *=-1
            else:
                output.append(abs(n))
        return output
    



# class Solution:
#     def findDuplicates(self, nums: 'List[int]') -> 'List[int]':
#         output = []
#         for n in nums: #mark the one traversed as negative number. If meets it again, it's a duplicated number
#             loc = abs(n)-1
#             if nums[loc] > 0:
#                 nums[loc] *= -1
#             else:
#                 output.append(abs(n)) # if the loc has been marked, the number was seen before
#         return output


# previous approach
# class Solution:
#     def findDuplicates(self, nums: 'List[int]') -> 'List[int]':
#         output = []
#         for n in nums: #use n as the index to check if the same index has been marked
#             if nums[abs(n)-1] < 0 : #current number is seen before
#                 output.append(abs(n))
#             else:
#                 nums[abs(n)-1] *= -1
#         return output


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
