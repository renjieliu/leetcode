def convertToBase7(num):
    """
    :type num: int
    :rtype: str
    """
    if num ==0:
        return "0"

    else :
        output = ""
        n = abs(num)
        while n>0:
            output = str(n%7) + output
            n //=7
        return output if num >= 0 else "-" + output

print(convertToBase7(1))


