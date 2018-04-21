def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    map = dict()
    for i in range(65, 91):
        map[chr(i)] = i-64
    # if len(s) == 1:
    #     return map[s]
    # else:
    pos = 0
    sum = 0
    for i in range(len(s)-1,-1, -1):
        sum += map[s[i]] * (26**pos)
        pos+=1
    return sum

print(titleToNumber("AZZ"))



