def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    temp = ""
    output = list()
    for i in digits:
        temp+=str(i)

    for i in str(int(temp) + 1):
        output.append(int(i))

    return output


print(plusOne([4,3,2,1]))


