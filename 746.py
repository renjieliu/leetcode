def minCostClimbingStairs(cost: 'List[int]'):
    if len(cost) == 0:
        return 0
    elif len(cost) in [1, 2]:
        return min(cost)

    a0 = cost[0]
    a1 = cost[1]
    for i in range(2, len(cost)):
        a2 = cost[i] + min(a0, a1)
        a0 = a1
        a1 = a2

    return min(a1, a0)


print(minCostClimbingStairs([10, 15, 20]))
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
