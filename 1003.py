def isValid(S: str):
    base = 'abc'
    if S.find(base)==-1 or len(S)%3 != 0:
        return False
    while S.find(base)!= -1:
        S=S.replace(base, "")
    return True if len(S)==0 else False



print(isValid("aabcbc"))

