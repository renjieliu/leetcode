def lengthOfLIS(nums: 'List[int]'):
    if len(nums) in [0,1]:
        return len(nums)
    long = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j]<nums[i]:
                long[i] = max( long[j] +1, long[i] )

    return max(long)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([1,1]))
print(lengthOfLIS([]))
print(lengthOfLIS([-2, -1]))
print(lengthOfLIS([-2, -2]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6])) #6