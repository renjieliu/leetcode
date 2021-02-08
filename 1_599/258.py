def add(num):
    x=list(str(num))
    sum = 0
    for i in range(0, len(x)):
        sum+=int(x[i])

    return sum


def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    t = add(num)
    while t >= 10:
        t=add(t)
    else:
        return t

print(addDigits(38))
