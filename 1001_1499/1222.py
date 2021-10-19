def queensAttacktheKing(queens: 'List[List[int]]', king: 'List[int]'):
    output = []
    for i in range(king[0] - 1, -1, -1):
        curr = [i, king[1]]
        if curr in queens:
            output.append(curr)
            break

    for i in range(king[0] + 1, 8):
        curr = [i, king[1]]
        if curr in queens:
            output.append(curr)
            break

    for i in range(king[1] - 1, -1, -1):
        curr = [king[0], i]
        if curr in queens:
            output.append(curr)
            break

    for i in range(king[1] + 1, 8):
        curr = [king[0], i]
        if curr in queens:
            output.append(curr)
            break

    for j in range(8):
        curr = [king[0] - j, king[1] - j]
        if curr in queens:
            output.append(curr)
            break

    for j in range(8):
        curr = [king[0] - j, king[1] + j]
        if curr in queens:
            output.append(curr)
            break

    for j in range(8):
        curr = [king[0] + j, king[1] - j]
        if curr in queens:
            output.append(curr)
            break

    for j in range(8):
        curr = [king[0] + j, king[1] + j]

        if curr in queens:
            output.append(curr)
            break

    return output


print(queensAttacktheKing(queens=[[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], king=[0, 0]))
print(queensAttacktheKing(queens=[[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], king=[3, 3]))
print(queensAttacktheKing(
    queens=[[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4],
            [2, 2], [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2],
            [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]], king=[3, 4]))
