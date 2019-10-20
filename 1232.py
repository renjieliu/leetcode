def checkStraightLine(coordinates: 'List[List[int]]'):
    p1 = coordinates[0]
    p2 = coordinates[1]

    if p2[0] == p1[0]:
        for c in coordinates:
            if c[0] != p1[0]:
                return False

    else:
        k = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b = p1[1] - k* p1[0]
        for i in coordinates:
            if i[1] != i[0]*k + b:
                return False


    return True



print(checkStraightLine( [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(checkStraightLine( [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
print(checkStraightLine( [[2,2], [2,3], [2,5]]))


