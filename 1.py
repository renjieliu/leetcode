def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    output = []
    for i in range(0, len(nums)):
        if target - nums[i] in list(nums) and list(nums).index(target - nums[i]) != i:
            output.append(i)
            output.append(list(nums).index(target - nums[i]))
            break

    return output


print(twoSum([2, 7, 11, 15],9))

