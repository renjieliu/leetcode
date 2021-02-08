def fact(n):
    output = 1
    for i in range(1,n+1):
        output*=i
    return output


def numberOfBoomerangs( points: 'List[List[int]]'):
    cnt  = 0
    for i in range(len(points)):
        curr = points[i]
        rest = points[:i] + points[i+1:]
        map_distance = {}
        c = 0
        for j in rest:
            d = (curr[0] - j[0]) ** 2 + (curr[1] - j[1]) ** 2  # If the **2 is the same, the sqrt should be the same as well.
            if d not in map_distance:
                map_distance[d] = 0
            map_distance[d] += 1

        for v in map_distance.values():
            if v >1:
                cnt+=fact(v)/fact(v-2)



    return int(cnt)

print(numberOfBoomerangs([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[8,0],[96,0],[76,0],[86,0],[56,0],[16,0]])) #32
print(numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1]])) #8
print(numberOfBoomerangs([[0,0],[1,0],[2,0]])) #2
print(numberOfBoomerangs([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8]])) #24




