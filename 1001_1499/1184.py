def distanceBetweenBusStops(distance: 'List[int]', start: int, destination: int):
    if start == destination:
        return 0

    s_1 = 0
    i = start
    curr = i % len(distance)
    while curr != destination:
        s_1 += distance[curr]
        i += 1
        curr = i % len(distance)

    s_2 = 0
    curr = start
    while curr != destination:
        curr-=1
        if curr < 0:
            curr = len(distance) + curr

        s_2 +=distance[curr]

    return min(s_1, s_2)


print(distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=1))  # 1
print(distanceBetweenBusStops([1, 2, 3, 4], start=0, destination=2))  # 3
print(distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=3))  # 4
print(distanceBetweenBusStops([7, 10, 1, 12, 11, 14, 5, 0], 7, 2))  #17


