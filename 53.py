def maxSubArray(nums: 'List[int]'):
    max = nums[0]
    for i in range(len(nums)):
        sum = nums[i]
        if sum > max:
            max = sum

        for j in range(i+1, len(nums)):
            sum+= nums[j]
            if sum > max:
                max = sum



    return max



print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([-2, 1]))
print(maxSubArray([-1,0,-2]))

print(maxSubArray(
    [-2, 1, -3, 4, -1, 2, 1, -5, 4, 6, 7, 8, 9, 0, -1, -1, 2, 4, 5, -4, 4, 32, 532, 5, -325, 23, 52, 45, 2]))


