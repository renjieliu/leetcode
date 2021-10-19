def rob(nums: 'List[int]'):
    if len(nums)==0:
        return 0
    elif len(nums)==1:
        return nums[0]
    elif len(nums)==2:
        return max(nums[0], nums[1])
    opt = [0]*3

    opt[0] = nums[0]
    opt[1] += max(opt[0], nums[1])

    for i in range(2, len(nums)):
        opt[2] = max(nums[i] + opt[0], opt[1])
        opt[0] = opt[1]  #shift the position after calculation
        opt[1] = opt[2]

    return opt[2]


print(rob([1,2,3,1]))
print(rob([1,1]))
print(rob([0]))
print(rob([]))
print(rob([2,7,9,3,1]))