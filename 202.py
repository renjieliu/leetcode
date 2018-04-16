def calc(n):
    x=list(str(n))
    sum = 0
    for i in range(0, len(x)):
        sum += int(x[i])**2
    return sum


def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    h = calc (n)
    dict = list()
    while h != 1:
        if h not in dict:
            dict.append(h)
            h=calc(h)
        else:
            return False
    else:
        return True

print(isHappy(68))


