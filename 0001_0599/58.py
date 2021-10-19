def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    return len(str(s).strip().split(" ")[-1])