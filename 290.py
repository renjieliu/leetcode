def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool

    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.

    """
    words =  str.split(" ")
    map= {}

    if len(words) != len(pattern) or len(set(list(pattern))) != len(set(str.split(" "))):
        return False

    else:
        for i in range(0, len(pattern)):
            if pattern[i] not in map:
                map[pattern[i]] = words[i]
            else:
                if map[pattern[i]] != words[i]:
                    return False
        return True

print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
print(wordPattern("aaaa", "dog cat cat dog"))
print(wordPattern("abba", "dog dog dog dog"))



