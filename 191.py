def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    sum = 0
    for i in bin(n).replace("0b",""):
        sum += int(i)
    return sum

print(hammingWeight(11))
print(hammingWeight(128))

