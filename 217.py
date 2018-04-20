def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    x=sorted(list(nums))
    for i in range(1, len(x)):
        if x[i] ==x[i-1]:
            return True


    return False


print(containsDuplicate([1,2,3,4]))