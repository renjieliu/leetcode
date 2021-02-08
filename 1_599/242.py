def isAnagram(s, t):
    s1 = list(str(s))
    t1 = list(str(t))

    s1.sort()
    t1.sort()

    if len(s1) != len(t1):
        return False
    else:
        output = True
        for i in range(0, len(s1)):
            if s1[i]!=t1[i]:
                output = False
                break
    return output


print(isAnagram("anagram", "nagaram"))



