def uncommonFromSentences(A: 'str', B: 'str'):
    dictA = {}
    dictB = {}
    output = []

    for i in A.split(" "):
        if i not in dictA.keys():
            dictA[i] = 1
        else:
            dictA[i] +=1

    for i in B.split(" "):
        if i not in dictB.keys():
            dictB[i] = 1
        else:
            dictB[i] +=1

    for k,v in dictA.items():
        if v==1 and k not in dictB.keys():
            if len(k) > 0:
                output.append(k)

    for k, v in dictB.items():
        if v == 1 and k not in dictA.keys():
            if len(k) > 0:
                output.append(k)

    return output


print(uncommonFromSentences("this apple is sweet",  "this apple is sour"))
print(uncommonFromSentences("apple apple", "banana"))
print(uncommonFromSentences("apple apple", ""))
