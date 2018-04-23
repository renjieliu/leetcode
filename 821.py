def shortestToChar(S, C):
    """
    :type S: str
    :type C: str
    :rtype: List[int]
    """

    output = list()
    position = [i for i in range(0, len(S)) if S[i] == C ]

    for i in range(0, len(S)):
        if S[i] ==C:
            output.append(0)
        else:
            min = abs(i-position[0])
            for j in position:
                if abs(i-j)<min:
                    min = abs(i-j)
            output.append(min)

    return  output

print(shortestToChar("loveleetcode", "e"))

