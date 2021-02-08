def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    pos = -1

    if len(needle) > len(haystack):
        return -1

    elif needle == haystack or len(needle) == 0:
        return 0

    else:
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                pos = i
                break
    return pos


print(strStr("abc", "b"))