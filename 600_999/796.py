def rotateString(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    output = False

    if A=="" and B=="":
        output = True

    else:
        for i in range(0, len(A)):
            print(A[i:] + A[0:i])
            if str(A[i:] + A[0:i]) == str(B):
                output= True
                break

    return output

print(rotateString("", ""))


