def numberOfSubarrays(nums: 'List[int]', k: int):
    # count the even number before each odd
    cnt = 0
    lkp = []
    for i in range(len(nums)):
        n = nums[i]
        if n % 2 == 0:
            cnt += 1
        else:
            lkp.append(cnt)
            cnt = 0

    lkp.append(cnt)  # for the last number

    output = 0

    for i in range(len(lkp) - k):
        temp = (lkp[i] + 1) * (lkp[i + k] + 1)
        output += temp

    return output


print(numberOfSubarrays([2,2,2,1,2,2,1,2,2,22,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,22,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,22,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,22,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,22,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,22,2,2,1,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,1,2,2]
,2)) #627