def allCellsDistOrder(R: int, C: int, r0: int, c0: int):
    map = {}
    for r in range(R):
        for c in range(C):
            distance = abs(r-r0) + abs(c-c0)
            if distance not in map:
                map[distance] = []
            map[distance].append([r,c])

    keys = sorted(map.keys())

    output = []

    for i in keys:
        for j in map[i]:
            output.append(j)
    return output






print(allCellsDistOrder( R = 1, C = 2, r0 = 0, c0 = 0))
print(allCellsDistOrder( R = 2, C = 2, r0 = 0, c0 = 1))
print(allCellsDistOrder( R = 2, C = 3, r0 = 1, c0 = 2))