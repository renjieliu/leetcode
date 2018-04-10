def rotate(nums, k):
    return nums[len(nums)-k:len(nums)] + nums[0:len(nums)-k]
print(rotate([1,2],1))


