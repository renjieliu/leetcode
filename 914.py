def hasGroupsSizeX(deck: 'List[int]'):
    if len(deck)<2:
        return False

    map = {}
    for i in deck:
        if i not in map :
            map[i] = 0
        map[i] +=1

    least = min(map.values())

    if least < 2 :
        return False

    for i in range(2, least+1):
        cnt = 0
        for v in map.values():
            if v%i ==0:
                cnt +=1

        if cnt ==len(map.values()):
            return True


    return False





print(hasGroupsSizeX([1,2,3,4,4,3,2,1]))
print(hasGroupsSizeX([1,1,1,2,2,2,3,3]))
print(hasGroupsSizeX([1]))
print(hasGroupsSizeX([1,1]))
print(hasGroupsSizeX([1,1,2,2,2,2]))
print(hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2]))


