def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    map = {
        "U":1,
        "D":-1,
        "L":-0.5,
        "R":0.5
     }

    sum = 0
    for i in range(0, len(moves)):
        sum+=map[moves[i]]

    if sum ==0:
        return True
    else:
        return False

print(judgeCircle("LLUURDD"))
