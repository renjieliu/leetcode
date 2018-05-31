def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    map = {
        "I": 1
        , "V": 5
        , "X": 10
        , "L": 50
        , "C": 100
        , "D": 500
        , "M": 1000
    }
    pos = 0
    output = 0

    while pos<len(s)-1:
        if s[pos]=="I" and s[pos+1] == "V":
            output+=4
            pos+=2

        elif s[pos]=="I" and s[pos+1] == "X":
            output+=9
            pos+=2
        elif s[pos] == "X" and s[pos + 1] == "L":
            output += 40
            pos += 2
        elif s[pos] == "X" and s[pos + 1] == "C":
            output += 90
            pos += 2

        elif s[pos] == "C" and s[pos + 1] == "D":
            output += 400
            pos += 2

        elif s[pos] == "C" and s[pos + 1] == "M":
            output += 900
            pos += 2
        else:
            output+= map[s[pos]]
            pos+=1

    return output + (map[s[-1]] if pos == len(s)-1 else 0 )

print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
print(romanToInt("MDCXCV"))











