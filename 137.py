def singleNumber(nums: 'List[int]') -> int:
    map = {}
    for i in nums:
        if i not in map:
            map[i] = 0
        map[i] += 1

    for k, v in map.items():
        if v == 1:
            return k

print(singleNumber([2,2,3,2]))