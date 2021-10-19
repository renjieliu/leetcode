def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    cnt = 0

    for i in range(0, len(J)):
        cnt += S.count(J[i])
    return cnt

print(numJewelsInStones("z", "ZZ"))



