def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    output = False
    for i in range(0, len(s)//2):
        temp = s
        if len(s)%(i+1) != 0:
            continue
        elif len(temp.replace(s[0:i+1],"")) == 0:
            output = True
            break

    return output



print(repeatedSubstringPattern("abab"))


