def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dict = {}

    for i in nums:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

    for k, v in dict.items():
        if v != 2:
            return k

