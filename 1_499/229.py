def majorityElement(nums: 'List[int]'):
    if len(nums) in [0,1]:
        return nums

    c1=float('inf')
    c2=float('inf')
    c1_cnt =0
    c2_cnt =0

    for i in range(len(nums)):
        if nums[i] == c1:
            c1_cnt +=1

        elif nums[i] ==c2:
            c2_cnt +=1

        elif c1_cnt==0:
            c1 = nums[i]
            c1_cnt +=1

        elif c2_cnt==0:
            c2 = nums[i]
            c2_cnt +=1

        else:
            c1_cnt -=1
            c2_cnt -=1


    c1_cnt =0
    c2_cnt =0

    for i in nums :
        if i ==c1:
            c1_cnt+=1
        elif i ==c2:
            c2_cnt +=1

    output = []
    if c1_cnt > len(nums)//3:
        output.append(c1)

    if c2_cnt> len(nums)//3:
        output.append(c2)

    return output

print(majorityElement([3,2,3]))
print(majorityElement([1,2]))
print(majorityElement([1,1,1,2,3,4,5,6]))
print(majorityElement([1,1,1,3,3,2,2,2]))