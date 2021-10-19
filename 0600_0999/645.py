class Solution:
    def findErrorNums(self, nums: 'List[int]') -> 'List[int]':
        total = ( 1+len(nums) ) * len(nums) //2
        curr = sum(nums)
        lkp = set()
        dup = None
        for n in nums:
            if n not in lkp:
                lkp.add(n)
            else:
                dup = n
                break
        missing = total - (curr - dup)
        return [dup, missing]


# previous approach
# def findErrorNums(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     map = {}
#     curr_sum = 0
#     for i in nums:
#         if i not in map:
#             map[i] = 1
#         else:
#             dups = i
#         curr_sum += i
#
#     ref_sum = (1+len(nums))*len(nums)/2
#
#     missing = dups - (curr_sum - ref_sum)
#
#     return [dups, int(missing)]
#
# print(findErrorNums([1,2,4,4]))
