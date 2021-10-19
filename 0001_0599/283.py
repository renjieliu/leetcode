def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0  # the last zero position
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]  # swap the current position with last 0 position
            i += 1

#     cnt = 0
#     t = list()
#     for i in nums:
#         if i == 0:
#             cnt += 1
#             t.append(i)
#     for i in t:
#         nums.remove(i)
#
#     for i in range(0, cnt):
#         nums.append(0)
#
#     return nums
#
#
# print(moveZeroes([0,1,0,3,-12]))
#
#
#
#
