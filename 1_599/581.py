def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    x = sorted(nums)
    start = 0
    end = 0
    for i in range(0, len(nums)):
        if nums[i] != x[i]:
            start = i
            break

    if nums[-1] != x[-1]:
        end = len(nums) -1

    else:
        for i in range(len(nums)-1, start-1, -1):
            if nums[i] != x[i]:
                end = i
                break

    return end - start +1 if end != start else 0


print(findUnsortedSubarray([2,8,7,4,8, 9]))
print(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(findUnsortedSubarray([1,2,3,4]))
print(findUnsortedSubarray([4,3,2,1]))

