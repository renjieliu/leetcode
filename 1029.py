def getKeys( hash, targetValue):
    output = []
    for k, v in hash.items():
        if v == targetValue:
            output.append(k)
    return output


def twoCitySchedCost(costs: 'List[List[int]]') -> int:
    map = {}
    for i in range(len(costs)):
        map[i] = costs[i][0] - costs[i][1]

    val = sorted(set(map.values()))
    cnt = 0
    s = 0
    for i in val:
        for k in getKeys(map, i):
            if cnt < len(costs) // 2:
                s += costs[k][0]
            else:
                s += costs[k][1]
            cnt += 1
    return s

#Below Code also works, in a more elegant way.

# def twoCitySchedCost(costs: 'List[List[int]]'):
#     costs = sorted(costs, key= lambda x : x[0]- x[1] )
#     output = 0
#     cnt = 0
#     for i in range(len(costs)):
#         if cnt < len(costs)//2:
#             output += costs[i][0]
#         else:
#             output +=costs[i][1]
#         cnt += 1
#     return  output
#





print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
print(twoCitySchedCost([[945,563],[598,753],[558,341],[372,54],[39,522],[249,459],[536,264],[491,125],[367,118],[34,665],[472,410],[109,995],[147,436],[814,112],[45,545],[561,308],[491,504],[113,548],[626,104],[556,206],[538,592],[250,460],[718,134],[809,221],[893,641],[404,964],[980,751],[111,935]]))
#7542