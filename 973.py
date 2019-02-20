def kClosest(points: 'List[List[int]]', K: 'int'):
    dic = {}
    distance  = []
    for i in points:
        dic[(i[0]**2 + i[1]**2 )**0.5 ] = i #use the distance as  key
        distance.append((i[0]**2 + i[1]**2 )**0.5 ) #push the value to a list

    distance.sort()
    pick = distance[:K] #get the first K points

    output = []

    for i in pick:
        output.append(dic[i]) #lookup the distance in the hash, and get the point out.

    return output

print(kClosest([[3,3],[5,-1],[-2,4]], 2))


