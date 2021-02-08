def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    output = ""

    while n>0:
        n-=1
        output = chr(int(n%26) + 65) + output
        n //=26

    return output


print(convertToTitle(26))
