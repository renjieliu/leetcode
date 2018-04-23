def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    t = magazine
    if ransomNote =="":
        return True
    else:
        for x in ransomNote:
            if x in t:
                t=t.replace(x, "", 1)
            else:
                return False

        return True


print(canConstruct("aa", "ab"))
print(canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))