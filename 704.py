def search(nums: 'List[int]', target: int):
    L = 0
    R = len(nums)
    if target>nums [-1] or target<nums[0]:
        return -1
    while L<=R:
        mid= (L+R)//2
        if nums[mid]>target:
            R=mid-1
        elif nums[mid]<target:
            L=mid+1
        elif nums[mid]==target:
            return mid

    return -1


print(search(nums = [-1,0,3,5,9,12], target = 9))
print(search(nums = [-1,0,3,5,9,12], target = 2))
print(search(nums = [-1,0,3,5,9,12], target = 13))
