def isOneBitCharacter(bits):
    """
    :type bits: List[int]
    :rtype: bool
    """
    s= ""
    for i in range(0, len(bits)-1):
        s+=str(bits[i])

    s1=s.replace("10","2").replace("11","3")
    s2=s.replace("11", "3").replace("10", "2")
    if s1.find("1")== -1 or s2.find("1") == -1 :
        return True
    else:
        return False

print(isOneBitCharacter([1, 0, 0]))
print(isOneBitCharacter([1, 1, 1, 0]))
print(isOneBitCharacter([1, 1, 0, 0]))


