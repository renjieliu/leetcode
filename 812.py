def size(point1, point2, point3):
    return abs(0.5*(point1[0]*point2[1] +point2[0]*point3[1] + point3[0]*point1[1] - point1[0]*point3[1] - point2[0]* point1[1] - point3[0]*point2[1]  ))


def largestTriangleArea(points):
    """
    :type points: List[List[int]]
    :rtype: float
    """
    maxsize = 0
    for i in range(0, len(points)):
        for j in range(i+1,len(points)):
            for k in range(i+2, len(points)):
                if size(points[i],points[j],points[k])> maxsize:
                    maxsize = size(points[i],points[j],points[k])
    return  maxsize



print(largestTriangleArea([[10,7],[0,4],[5,7]]))
print(largestTriangleArea( [[0,0],[0,1],[1,0],[0,2],[2,0]]))
