def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 1
    while i<len(nums):
        if nums[i]==nums[i-1]:
            nums.pop(i)
            i-=1
        i+=1
    # print(nums)
    return len(nums)

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))