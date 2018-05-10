def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    x = 1
    t=num
    while x < 100 :
        t = 0.5*(t + num/t)
        x+=1
    if t-t//1 ==0 :
        return True
    else:
        return False

print(isPerfectSquare(15))

