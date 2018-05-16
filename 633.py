def judgeSquareSum(c):
    """
    :type c: int
    :rtype: bool
    """
    for i in range(0,int(c**0.5)+1):
        if int((c-i**2)**0.5) ==(c-i**2)**0.5:
            return True
    return False


print(judgeSquareSum(5))
print(judgeSquareSum(0))
print(judgeSquareSum(3))
print(judgeSquareSum(4294967296))


