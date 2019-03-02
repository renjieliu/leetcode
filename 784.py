def cartesian(a, b):
    output = []
    if len(a)==0: return b
    if len(b)==0: return a

    else:
        for i in a:
            for j in b:
                output.append(str(i) + str(j))
    return output


def letterCasePermutation(S: str):
    t =  []
    for i in range(len(S)):
        if 65 <=ord(S[i]) <=90:
            t.append([S[i], chr(ord(S[i])+32)])

        elif 97<=ord(S[i]) <=122:
            t.append([S[i], chr(ord(S[i]) -32)])

        else:
            t.append([S[i]])
    print(t)
    if len(t) ==0: return [""]
    elif len(t) == 1:return cartesian(t[0], '')
    elif len(t) == 2:return cartesian(t[0], t[1])

    else:
        temp = cartesian(t[0], t[1])
        for i in range(2, len(t)):
            temp = cartesian(temp, t[i])

    return temp


print(letterCasePermutation(""))
print(letterCasePermutation("a"))
print(letterCasePermutation("C"))
print(letterCasePermutation("8"))
print(letterCasePermutation("a1"))
print(letterCasePermutation("a1b"))
print(letterCasePermutation("a1b2"))