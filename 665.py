def checkPossibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    cnt = 0
    pos = None
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            cnt +=1
            pos = i
            if cnt >=2:
                return False

    if cnt == 0:
        return True
    else:
        if pos==0 or pos ==len(nums)-2 or nums[pos+1] >= nums[pos-1] or nums[pos] <=nums[pos+2]:
            return True
    return False





    #         print('x2-', x2)
    #
    # print('cnt_1-', cnt_1)
    # print('cnt_2-', cnt_2)
    # print(x1)
    # print(x2)



print(checkPossibility([4,2,3]))#t
print(checkPossibility([1,4,2,3])) #t
print(checkPossibility([4,2,1])) #f
print(checkPossibility([1,3,2])) #t
print(checkPossibility([3,4,2,3])) #f
print(checkPossibility([2,3,3,2,4])) #t






