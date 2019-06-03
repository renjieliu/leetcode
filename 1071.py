def gcdOfStrings(str1: str, str2: str):
    short = str1 if len(str1) < len(str2) else str2
    long  = str1 if short ==str2 else str2

    for i in range(len(short),-1,-1):
        t = short[:i]
        if short.replace(t,'') ==long.replace(t,'') == '':
            return t

    return ''


print(gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
print(gcdOfStrings(str1 = "LEET", str2 = "CODE"))

