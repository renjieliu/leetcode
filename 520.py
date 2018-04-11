def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    output = False
    lower = 0
    upper = 0
    for i in range(0, len(word)):
        if ord(word[i]) >= 97:
            lower += 1
        else:
            upper += 1
    if (lower ==len(word) or upper == len(word)) or ((ord(word[0])<97 and lower == len(word) -1)):
        output = True

    return output


print(detectCapitalUse("Google"))
print(detectCapitalUse("GOOGLE"))
print(detectCapitalUse("g"))
print(detectCapitalUse("apple"))
print(detectCapitalUse("apPle"))





