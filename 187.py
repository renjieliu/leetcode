def findRepeatedDnaSequences(s: str):
    if len(s)<=10:
        return []

    output = set()
    temp = {}
    for i in range(len(s)-9):
        t = s[i:i+10]
        if t not in temp.keys():
            temp[t] =1
        else:
            output.add(t)


    return list(output)

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(findRepeatedDnaSequences("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))
print(findRepeatedDnaSequences("AAAAAAAA"))


