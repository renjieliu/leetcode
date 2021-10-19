def intervalIntersection(A: 'List[List[int]]', B: 'List[List[int]]'):
    A.sort()
    B.sort()
    i = 0
    s = 0
    output = []
    for a in A:
        i = s
        while i < len(B):
            b=B[i]
            if b[0] <= a[0] <= b[1]:
                output.append([a[0], min(a[1], b[1])])
            elif b[0] <= a[1] <= b[1]:
                output.append([b[0], min(a[1], b[1])] )
            elif a[0] <= b[0] <=a[1]:
                output.append([ b[0],min(a[1], b[1]) ])
            elif a[0] > b[1]:
                s = i
            i+=1
    return output

print(intervalIntersection( A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]) )
print(intervalIntersection([[3,5],[9,20]],
[[4,5],[7,10],[11,12],[14,15],[16,20]]) ) #[[4,5],[9,10],[11,12],[14,15],[16,20]]
