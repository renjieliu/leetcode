def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    row = {
        "q": 1,
        "w": 1,
        "e": 1,
        "r": 1,
        "t": 1,
        "y": 1,
        "u": 1,
        "i": 1,
        "o": 1,
        "p": 1,
        "a": 2,
        "s": 2,
        "d": 2,
        "a": 2,
        "s": 2,
        "d": 2,
        "f": 2,
        "g": 2,
        "h": 2,
        "j": 2,
        "k": 2,
        "l": 2,
        "z": 3,
        "x": 3,
        "c": 3,
        "v": 3,
        "b": 3,
        "n": 3,
        "m": 3
    }

    output = list()
    for i in range(0, len(words)):
        curr = str(words[i]).lower()
        keyrow = row[curr[0]]
        for j in range(1, len(curr)):
            if row[curr[j]] != keyrow:
                keyrow = 9999
                break
        if keyrow != 9999:
            output.append(words[i])

    return output


print(findWords(["Hello", "Alaska", "Dad", "Peace"]))




