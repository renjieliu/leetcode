def findLUSlength(a, b):
    """
    :type a: str
    :type b: str
    :rtype: int
    """
    len1=0
    len2=0

    if a==b:
        return -1
    else:

        for i in range(len(a), -1 , -1 ):
            if a[0:i] not in b:
                len1 = i
                break

        for i in range(len(b), -1 , -1 ):
            if b[0:i] not in a:
                len2 = i
                break

        return len1 if len1>=len2 else len2

print( findLUSlength("cdc", "cdc"))