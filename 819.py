def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    dict = list("abcdefghijklmnopqrstuvwxyz ")
    x = str(paragraph).lower()
    cleaned = ""
    for i in range(0, len(x)):
        if x[i] in dict:
            cleaned += x[i]
    y = cleaned.split(" ")
    print(y)
    map = {}
    for j in y:
        if j not in banned and j not in map:
            map[j] = 1
        elif j in map:
            map[j] +=1
    max = 0
    output = ""
    for k, v in map.items():
        if v>max:
            output = k
            max = v
    return output

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))


