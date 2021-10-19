def hasAlternatingBits(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 1:
        return True
    else:
        x = str(bin(n)).replace("0b","")
        for i in range(1, len(x)):
            if abs(int(x[i-1])-1) != abs(int(x[i])):
                return False

        return True


print(hasAlternatingBits(7))