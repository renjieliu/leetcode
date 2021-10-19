def reverseStr(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """

    output = ""
    cnt = 0
    temp = ""
    for i in range(0, len(s)):
        cnt+=1
        if cnt < k:
            temp +=s[i]
            if i==len(s) - 1:
                output+= temp[::-1]
                return output

        elif cnt == k:
            temp += s[i]
            temp = temp[::-1]
            output += temp
            temp = ""

        elif cnt >k and cnt < 2*k:
            temp = ""
            output +=s[i]
        elif cnt == 2*k:
            temp = ""
            output += s[i]
            cnt = 0

    return output

print(reverseStr("abcdefg",2)) #bacdfeg
print(reverseStr("123456789123456789",3)) #bacdfeg




