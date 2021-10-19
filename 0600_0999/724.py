def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum_total = 0
    for i in nums:
        sum_total += i

    sum_curr = 0
    for i in range(0, len(nums)):

        if sum_curr == (sum_total-nums[i])/2:
            return i
        else:
            sum_curr+=nums[i]
    return -1

print(pivotIndex([1, 7, 3, 6, 5, 6]))
print(pivotIndex([1, 2, 3]))
