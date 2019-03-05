def findKey(map: 'dict', value):
    output = []
    for k, v in map.items():
        if v == value:
            output.append(k)
    return output


def topKFrequent(nums: 'List[int]', k: int):
    map = {}
    output = []
    for i in nums:
        if i not in map.keys():
            map[i] = 0
        map[i] += 1

    max = 0
    min = float('inf')
    for i in map.values():
        if i > max:
            max = i
        if i < min:
            min = i
    #bucket sort
    bucket = [None] * (max + 1)

    for i in map.values():
        bucket[i] = i

    sortedlist = []
    for i in range(len(bucket)-1,-1,-1):
        if bucket[i] != None:
            sortedlist.append(bucket[i])

    for i in range(k):
        for x in findKey(map, sortedlist[i]):
            output.append(x)
        if len(output) >=k:
            return output

    return output


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1, 1, 1, 2, 2, 3,3], 3))
print(topKFrequent([1], 1))
print(topKFrequent([5,3,1,1,1,3,73,1],2))
