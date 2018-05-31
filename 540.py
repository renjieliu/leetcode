def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cnt = 0
    for i in range(len(nums) - 1):
        cnt += 1
        if cnt == 2:
            if nums[i] != nums[i - 1]:
                return nums[i - 1]
            else:
                cnt = 0
    return nums[-1]


print(singleNonDuplicate([1,1,2]))
print(singleNonDuplicate([1,2,2]))
print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(singleNonDuplicate([3,3,7,7,10,11,11]))


