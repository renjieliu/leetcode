class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        hmp = {}
        for i , n in enumerate(nums):
            if n not in hmp:
                hmp[n] = []
            hmp[n].append(i)
        for i , n in enumerate(nums):
            if target - n in hmp:
                if n == target-n:
                    if len(hmp[n]) == 2:
                        return hmp[n]
                else:
                    return [i, hmp[target-n][0]]


# previous approach
# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     output = []
#     for i in range(0, len(nums)):
#         if target - nums[i] in list(nums) and list(nums).index(target - nums[i]) != i:
#             output.append(i)
#             output.append(list(nums).index(target - nums[i]))
#             break
#
#     return output
#
#
# print(twoSum([2, 7, 11, 15],9))

