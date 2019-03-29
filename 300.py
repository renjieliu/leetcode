def lengthOfLIS(nums: 'List[int]'):
    if len(nums) in [0,1]:
        return len(nums)
    long = [None] * len(nums)
    long[0] = None

    for i in range(len(nums)):
        find = 1
        tempMax = [-99]
        for j in range(i, -1, -1):
            if long[j] != None and nums[j]<nums[i]:
                tempMax.append(long[j]+find)

            elif nums[j]<nums[i]:
                find+=1

        long[i] =max(find, max(tempMax) )

    return max(long)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([1,1]))
print(lengthOfLIS([]))
print(lengthOfLIS([-2, -1]))
print(lengthOfLIS([-2, -2]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6])) #6