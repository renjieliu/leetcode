def productExceptSelf(nums: 'List[int]'):
    #from left to right, make the first element as 1.
    ini =1
    output =[]
    for i in range(len(nums)):
        output.append(ini)
        ini*=nums[i]

    #from right to left

    ini = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] = output[i] * ini
        ini *= nums[i]
    return output

print(productExceptSelf([1,2,3,4]))