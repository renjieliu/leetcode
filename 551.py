def checkRecord(s):
    """
    :type s: str
    :rtype: bool
    """

    return True if len(str(s)) - len(str(s).replace("A","`").replace("LLL","|").replace("`","").replace("|","")) <= 1 else False

print(checkRecord("LALL"))