def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    output = ""
    reg = 0

    n1 = a if len(a) >= len(b) else b
    n2 = a if len(a) < len(b) else b

    n2 = str(0) * (len(n1) - len(n2)) + n2

    for i in range(len(n2)-1, -1, -1):
        if int(n2[i]) + int(n1[i]) + int(reg) > 1:
            output = str( ( int(n2[i]) + int(n1[i]) + int(reg) ) %2) + output
            reg = 1

        else:
            output = str( int(n2[i]) + int(n1[i]) + int(reg) ) + output
            reg = 0

    return str(reg) + output if reg==1 else output

print(addBinary("1","11"))




















