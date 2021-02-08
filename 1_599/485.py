def findMaxConsecutiveOnes( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    temp = list()
    cnt = 0
    for i in range(0, len(nums)):
         if nums[i] ==1:
             cnt += 1
         else:
            temp.append(cnt)
            cnt = 0
         if i ==  len(nums) -1 :
             temp.append(cnt)
    return max(temp)

print(findMaxConsecutiveOnes( [1,1,0,1,1,1]))




