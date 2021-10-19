def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    map = {}
    for i in range(0, len(nums)):
        if nums[i] in map:
            map[nums[i]].append(i)
        else:
            map[nums[i]] = []
            map[nums[i]].append(i)

    for v in map.values():
        if len(v) <2:
            continue
        else:
            for i in range(1, len(v)):
                if v[i] - v[i-1] <= k:
                    return True

    return False



print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1],3))
print(containsNearbyDuplicate([1,2,1],0))
print(containsNearbyDuplicate([],9))


