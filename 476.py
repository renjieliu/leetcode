def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    b = str(bin(num)).replace("0b", "")
    b = b.replace("1","a").replace("0","1").replace("a","0")

    return int(b, 2)

print(findComplement(1))




