def isPowerOfThree(self, n):
    """
    :type n: int
    :rtype: bool
    """
    return n > 0 and 1162261467 % n == 0  # power of 3 should be able to be divided by the largest power3 which is < Int32.
