def isRectangleOverlap(rec1: 'List[int]', rec2: 'List[int]'):
    #[x1, y1, x2, y2] , [x1, y1, x2, y2]
    if rec1[0] >= rec2[2]or rec1[3] <= rec2[1] or rec1[2]<=rec2[0] or rec1[1]>=rec2[3]:
        return False
    elif rec2[0] >= rec1[2]or rec2[3] <= rec1[1]  or rec2[2] <= rec1[0] or rec2[1] >= rec1[3]:
        return False
    else:
        return True

print(isRectangleOverlap([0,0,2,2], [1,1,3,3]))
print(isRectangleOverlap([0,0,1,1], [1,0,2,1]))






