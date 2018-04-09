def reverseString(s):
    output = ""
    for i in range(len(s)-1, -1,-1):
        output += s[i]
    return  output

print(reverseString("Hello"))