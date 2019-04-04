def majorityElement(nums: 'List[int]'):
    map = {}
    for i in nums:
        if i not in map:
            map[i] = 0
        map[i]+=1

    output = []
    for k,v in map.items():
        if v>len(nums)//3:
            output.append(k)

    return output

print(majorityElement( [3,2,3]))
print(majorityElement( [1,1,1,3,3,2,2,2]))

