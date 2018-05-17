def countBinarySubstrings(s):
    """
    :type s: str
    :rtype: int
    """

    cnt_1 = 1
    cnt_2 = 0
    output = 0
    ref = s[0]

    for i in range(1, len(s)):
        if s[i]==ref and s[i] == s[i-1]:
            cnt_1 += 1

        elif s[i]!=ref:
            cnt_2 += 1

        elif s[i]==ref and s[i] != s[i-1]:
            output += (cnt_1 if cnt_1 <= cnt_2 else cnt_2)
            ref = s[i-1]
            cnt_1=cnt_2
            cnt_2 = 1

    output += (cnt_1 if cnt_1 <= cnt_2 else cnt_2)

    return output
#
print(countBinarySubstrings("00110011")) #6
print(countBinarySubstrings("10101")) #4
print(countBinarySubstrings("00110")) #3
print(countBinarySubstrings("00100010101010101010101010100110")) #27
print(countBinarySubstrings("00100010101010101010101010100110001000101010101010101010101001100010001010101010101010100000000000000000000011111111111111111101001100010001010101010101010101010011000100010101010101010101010100110")) #156
print(countBinarySubstrings("10")) #1



