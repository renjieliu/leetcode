def carPooling(trips: 'List[List[int]]', capacity: int):
    #[3, 2, 7], [8, 3, 9] , [3, 7, 9], 11
    unload = {}
    for i in trips:
        if i[2] not in unload:
            unload[i[2]] = 0
        unload[i[2]] += i[0]
    route = sorted(trips,key=lambda x: x[1])
    # print(route)
    # print(unload)
    curr = route[0][0]
    kick = [route[0][2]]

    for i in range(1,len(route)):
        temp = []
        for k in kick:
            if k <= route[i][1]:
                curr-=unload[k]
            else:
                temp.append(k)
        kick = temp.copy()
        curr += route[i][0]

        #print(curr)
        if curr > capacity:
            return False

        if route[i][2] not in kick:
            kick.append(route[i][2])


    return True


print(carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4))
print(carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5))
print(carPooling(trips = [[2,1,5],[3,5,7]], capacity = 3))
print(carPooling(trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11))
print(carPooling(trips = [[8,2,3],[4,1,3],[1,3,6],[8,4,6],[4,4,8]], capacity = 12))
print(carPooling(trips = [[3,2,8],[4,4,6],[10,8,9]], capacity = 11))