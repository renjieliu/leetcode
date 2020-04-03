def maxSubArray(self, nums: 'List[int]') -> int:
    dp =[nums[0]]
    for i in range(1, len(nums)):
        dp.append(max(dp[-1]+nums[i], nums[i]))
    return max(dp)


# print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(maxSubArray([-2, 1]))
# print(maxSubArray([-1,0,-2]))
#
# print(maxSubArray(
#     [-2, 1, -3, 4, -1, 2, 1, -5, 4, 6, 7, 8, 9, 0, -1, -1, 2, 4, 5, -4, 4, 32, 532, 5, -325, 23, 52, 45, 2]))


