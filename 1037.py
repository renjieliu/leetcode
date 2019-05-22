def distance(p1, p2):
    return ((p1[0] -p2[0]) **2  + (p1[1] -p2[1])**2)**0.5


def isBoomerang(points: 'List[List[int]]'):
    if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
        return False
    else:
        # print(distance(points[0],points[1]) , distance(points[1],points[2]), distance(points[0],points[2]))
        if distance(points[0],points[1]) +  distance(points[1],points[2]) > distance(points[0],points[2]) \
            and distance(points[0],points[2]) +  distance(points[0],points[1]) > distance(points[1],points[2]) \
            and distance(points[1],points[2]) +  distance(points[0],points[2]) > distance(points[0],points[1]):
            return True
        else:
            return False


print(isBoomerang([[1,1],[2,3],[3,2]]))
print(isBoomerang([[1,1],[2,2],[3,3]]))
print(isBoomerang([[0,0],[1,0],[2,2]]))
