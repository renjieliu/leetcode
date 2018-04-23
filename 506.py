def findRelativeRanks(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    output = list()
    t = sorted(nums, reverse=True)
    for i in nums:
        if t.index(i) == 0:
            output.append("Gold Medal")
        elif t.index(i) == 1:
            output.append("Silver Medal")
        elif t.index(i) == 2:
            output.append("Bronze Medal")
        else:
            output.append(str(t.index(i)-1))
    return output

print(findRelativeRanks([10,3,8,9,4]))