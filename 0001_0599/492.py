def constructRectangle(area):
    """
    :type area: int
    :rtype: List[int]
    """
    curr_min = area
    w = 0

    for i in range(1, int(area**0.5)+1):
        if area%i == 0:
            if area//i - i < curr_min:
                curr_min = area//i - i
                w = i
    return [area//w,w]

print(constructRectangle(4))
print(constructRectangle(10000000))
print(constructRectangle(991211))

