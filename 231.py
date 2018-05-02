def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n==0:
        return False
    else:
        return True if n&(n-1) == 0 else False

print(isPowerOfTwo(1))