def minCostToMoveChips(chips: 'List[int]'):
    s1, s2  = 0, 0
    for i in chips:
        s1+= 0 if abs((i-1))%2 ==0 else 1  # move everything to position 1
        s2+= 0 if abs((i - 2)) % 2 == 0 else 1 #move everything to position 2
    return min(s1, s2)



print(minCostToMoveChips(chips = [1,2,3]))
print(minCostToMoveChips(chips = [2,2,2,3,3]))
print(minCostToMoveChips(chips = [2,2,2,3,100000003]))
print(minCostToMoveChips(chips = [2,2,2,3,100000003,3,100000003,3,100000003,3,100000003,3,100000003,3,100000003,3,100000003,3,100000003,3,100000003,3,100000003,3,100000003,3,100000003,3,100000003,3,100000003,3,100000003,3,100000003]))