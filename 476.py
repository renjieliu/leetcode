def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    output = ""
    b = str(bin(num)).replace("0b", "")
    #print(b)
    for i in range(0, len(b)):
        output+= str(0) if b[i] == "1" else str(1)
    #print(output)
    return int(output, 2)

print(findComplement(0))




