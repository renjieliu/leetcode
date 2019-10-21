def sortColors(nums: 'List[int]'):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    length = len(nums)
    cnt = 0
    while i < length:
        #print(nums )
        cnt += 1
        if nums[i] == 0:
            del nums[i]
            nums.insert(0, 0)
            i+=1
        elif nums[i] == 2:
            del nums[i]
            nums.append(2)
        else:
            i += 1

        if cnt == length:
            break

    return nums


print(sortColors([2, 0, 2, 1, 1, 0]))
