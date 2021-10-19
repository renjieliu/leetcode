class Solution:
    def majorityElement(self, nums: 'List[int]') -> int:
        hmp = {}
        for n in nums:
            if n not in hmp:
                hmp[n] = 0
            hmp[n] += 1
        compare = len(nums) // 2
        for k, v in hmp.items():
            if v > compare:
                return k

# OLD SOLUTION
# def majorityElement(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     map = dict()
#     max = 0
#     output = 0
#     for i in nums:
#         if i not in map:
#             map[i] =1
#         else:
#             map[i] += 1
#         if map[i] > max:
#             max = map[i]
#             output = i
#
#     return output
#
# print(majorityElement([2,2,1,1,1,2,2]))
#
#
#
#
