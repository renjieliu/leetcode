def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    map = dict()
    max = 0
    output = 0
    for i in nums:
        if i not in map:
            map[i] =1
        else:
            map[i] += 1
        if map[i] > max:
            max = map[i]
            output = i

    return output

print(majorityElement([2,2,1,1,1,2,2]))




