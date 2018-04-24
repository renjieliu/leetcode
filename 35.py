def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i in range(0, len(nums)):
        if nums[i] >= target :
            return i

    return len(nums)


print(searchInsert( [1], 0) )



