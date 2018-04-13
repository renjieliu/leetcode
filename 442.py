def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dict  = {}
    output = list()
    for i in nums:
        if i in dict.keys():
            output.append(i)
        else:
            dict[i] = 0
    return output

print(findDuplicates([4,3,2,7,8,2,3,1]))
