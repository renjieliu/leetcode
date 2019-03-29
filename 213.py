def rob_try(nums: 'List[int]'):
    if len(nums) ==0:
        return 0
    elif len(nums) in [1,2]:
        return max(nums)
    else:
        opt = [0]*3
        opt[0] = nums[0]
        opt[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            opt[2] = max(opt[1], opt[0] + nums[i])
            opt[0] = opt[1]
            opt[1] = opt[2]

    return opt[-1]


def rob(nums: 'List[int]'):
    if len(nums) ==0:
        return 0
    elif len(nums) in [1,2]:
        return max(nums)
    else:
        return max( rob_try(nums[1:]), rob_try(nums[:-1]), rob_try(nums[1:-1]) )

print(rob([2,3,2]))
print(rob([1,2,3,1]))
print(rob([1]))
print(rob([4,1,2,7,5,3,1]))


