def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    temp = 1
    for i in range(1, 100):
        temp = 0.5*(temp+x/temp)
    return temp

print(mySqrt(200)//1)