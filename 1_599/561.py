def sort(nums):
    end = False
    while not end:
        end = True
        for i in range(0, len(nums)-1):
            if nums[i]>nums[i+1]:
                t=nums[i]
                nums[i] = nums[i+1]
                nums[i + 1] = t
                end  = False
    return nums


def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    X = list(nums)
    X.sort()
    sum = 0
    for i in range(0, len(X)-1, 2):
        sum += X[i]
    return sum


print(arrayPairSum([1,2,3,2]))