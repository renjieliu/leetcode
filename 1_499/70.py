def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    # if n == 1:
    #     return 1
    # elif n == 2 :
    #     return 2
    # else:
    #     return climbStairs(n-1) + climbStairs(n-2)
    # using loop to calculate fibonacci
    if n == 1 :
        return 1
    elif n == 2 :
        return 2
    else:
        first = 1
        second = 2
        for n in range(3, n+1):
            result = first+second
            first = second
            second = result
        return result

print (climbStairs(4))
