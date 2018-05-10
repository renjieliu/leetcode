def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    temp = []
    vowel = ['a','A','e','E','i','I','o','O','u','U']
    for i in range(0, len(s)):
        if s[i] in vowel:
            temp.append(s[i])
    output=""
    cnt = -1
    for i in range(0, len(s)):
        if s[i] in vowel:
            output+= temp[cnt]
            cnt -= 1
        else:
            output+= s[i]

    return output

print(reverseVowels("hello"))
print(reverseVowels("leetcode"))
