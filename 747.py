def dominantIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==1:
        return 0
    else:
        x = sorted(nums)
        if x[-1] >= 2*x[-2]:
            return nums.index(x[-1])
        else:
            return -1

print(dominantIndex( [1, 2, 3, 4]))

