def numberOfLines(widths, S):
    """
    :type widths: List[int]
    :type S: str
    :rtype: List[int]
    """
    dict = {}
    now = 97
    if len(S)>0:
        space = 0
        line = 1
        for i in list(S):
            if space + widths[ord(i)-97] >100:
                line += 1
                space = 0
                space += widths[ord(i)-97]
            else:
                space += widths[ord(i)-97]
        return [line, space]

    else:
        return [0,0]




print(numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],  "bbbcccdddaaa"))
