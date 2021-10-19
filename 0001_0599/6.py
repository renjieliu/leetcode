def convert(s: str, numRows: int):
    if numRows == 1:
        return s

    grid = [["" for _ in range(len(s))] for _ in range(numRows)]
    direction = 1  # down
    column = 1  # same column
    i = 0
    r = 0
    c = 0
    while i < len(s):
        if direction == 1 and column == 1:
            grid[r][c] = s[i]
            r += 1
        elif direction == 0 and column == 0:
            grid[r][c] = s[i]
            r -= 1
            c += 1

        if (r + 1) % numRows == 0:  # reach the bottom, need to go up.
            direction = 0  # go up
            column = 0  # different column

        elif r == 0:
            direction = 1
            column = 1

        i += 1

    output = ""

    for i in grid:
        for j in i:
            output += j

    return output


print(convert(s = "PAYPALISHIRING", numRows = 3))
print(convert(s = "PAYPALISHIRING", numRows = 4))
print(convert(s = "ABCD", numRows = 1))
print(convert(s = "A", numRows = 5))


