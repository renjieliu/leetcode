def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    map = {}
    map_2 = {}
    for i in range(len(s)):
        if s[i] not in map:
            map[s[i]]= t[i]
        else:
            if t[i]!=map[s[i]]:
                return False

    for i in range(len(t)):
        if t[i] not in map_2:
            map_2[t[i]]= s[i]
        else:
            if s[i]!=map_2[t[i]]:
                return False

    return True

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("", ""))
print(isIsomorphic("ab", "aa"))



