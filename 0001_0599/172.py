def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    if n<5:
        return 0
    else:

        x = int(n/5)//5 #5
        sum = int(n / 5) + x
        while x>=5:
            x//=5
            sum+=x
    return sum



print(trailingZeroes(1000))



