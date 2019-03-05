def singleNumber(nums: 'List[int]'):
    map = {}
    for i in nums:
        if i not in map.keys():
            map[i] = 0
        map[i]+=1

        if map[i] ==2:
            del map[i]

    return list(map.keys())

print(singleNumber([1,2,1,3,2,5]))