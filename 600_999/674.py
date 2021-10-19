def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) ==0:
        return 0

    else :

        cnt = 1
        max = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                if cnt > max:
                    max = cnt
                cnt = 1

        if cnt > max:
            max = cnt

        return max



print(findLengthOfLCIS([2,2,1,1,2,3,4]))
print(findLengthOfLCIS([]))


