def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_1 = nums[0]
    min_1 = nums[0]

    for i in nums:
        if i > max_1:
            max_1 = i

    for i in nums:
        if i < min_1:
            min_1 = i

    max_2 = min_1

    for i in nums:
        if i > max_2 and i< max_1:
            max_2 = i

    max_3 = min_1
    for i in nums:
        if i > max_3 and i < max_2 and i < max_1:
            max_3 = i

    x=(set([max_1, max_2, max_3]))
    return max_3 if len(x) >= 3 else max_1

print(thirdMax([0, 1 ]))
