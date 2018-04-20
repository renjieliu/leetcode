def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    cnt = 0
    t = list()
    for i in nums:
        if i == 0:
            cnt += 1
            t.append(i)
    for i in t:
        nums.remove(i)

    for i in range(0, cnt):
        nums.append(0)

    return nums


print(moveZeroes([0,1,0,3,-12]))




