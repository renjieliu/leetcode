def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    max = nums[0]
    count = 0
    for i in nums:
        sum+=i
        if i>max:
            max = i
    if max!=len(nums):
        return len(nums)
    else:
        ought =  max * (len(nums) +1) /2
        return int(ought-sum)


print(missingNumber([0]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))