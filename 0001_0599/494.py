def findTargetSumWays(nums: 'List[int]', S: int):
    if len(nums)==0:
        return 0
    temp = [None]*len(nums)
    if nums[0] ==0: temp[0] = {0:2}
    else: temp[0] = {nums[0]:1, -nums[0]:1}

    for i in range(1,len(nums)):
        temp[i] = {}
        for k, v in temp[i-1].items():
            if k + nums[i] in temp[i]: # this is to calcualte how many times the number has appeared in the current iteration.
                temp[i][k + nums[i]] = temp[i][k + nums[i]] + v
            else:
                temp[i][k + nums[i]] = v

            if k - nums[i] in temp[i]:
                temp[i][k - nums[i]] = temp[i][k - nums[i]] + v
            else:
                temp[i][k - nums[i]] = v

    return temp[-1][S] if S in temp[-1]  else 0

print(findTargetSumWays([1, 1, 1, 1, 1], 3))
print(findTargetSumWays([1, 1, 1, 1, 1], 27))
print(findTargetSumWays([45,18,27,39,42,19,1,35,32,16,7,6,25,41,27,18,38,6,42,10], 49))

