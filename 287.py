def findDuplicate(nums: 'List[int]'):
    map = {}
    for i in nums:
        if i not in map:
            map[i] = 1
        else:
            return i


print(findDuplicate([1,3,4,2,2]))
print(findDuplicate([1]))