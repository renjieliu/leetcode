def maxDistToClosest(seats: 'List[int]'):
    cnt = 0
    max = 0

    if seats[0] == 0:
        for i in seats:
            if i == 0:
                max += 1
            else:
                break

    for i in seats:
        if i == 0:
            cnt += 1
        else:

            distance = cnt // 2 if cnt % 2 == 0 else cnt // 2 + 1

            if max < distance:
                max = distance

            cnt = 0
    if i == 0 and max < cnt:  # the last seat is 0
        max = cnt

    return max


print(maxDistToClosest( [1,0,0,0,1,0,1]))
print(maxDistToClosest(  [1,0,0,0]))
print(maxDistToClosest(  [0,0,0,1]))
print(maxDistToClosest(  [0,0,0,0,1,0,0,1,1,1,0]))


