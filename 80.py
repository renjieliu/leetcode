def removeDuplicates( nums: 'List[int]'):
    if len(nums)<3:
        return len(nums)
    else:
        r_cnt = 0
        curr_cnt = 1
        i = 1

        while i < len(nums):
            if nums[i] == nums[i-1]:
                curr_cnt += 1
            else:
                curr_cnt = 1
            if curr_cnt > 2:
                r_cnt += 1
                nums.remove(nums[i])
                curr_cnt -= 1
            else:
                i+=1

    return len(nums)



nums = [1,1,1,2,2,3]
len = removeDuplicates(nums)
for i in range(len):
    print(nums[i])









